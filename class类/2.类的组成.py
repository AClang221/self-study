"""
类的组成：
    1.类属性：直接定义在类中方法外的变量
    2.实例属性：定义在_init_方法中，使用self打点的变量
    3.实例方法：定义在类中的函数，而且自带参数self
    4.静态方法：使用装饰器@staticmethod修饰的方法
    5.类方法：使用装饰器@classmethod修饰的方法
"""


class Student:
    # 类属性：定义在类中，方法外的变量
    school = "浙江经济职业技术学院"

    # 实例属性
    def __init__(self, xm, age):  # xm,age是方法的参数，是局部变量，说明xm和age的作用域就是整个__init__方法
        self.name = xm  # =左侧是实例属性，xm是局部变量，将局部变量的值xm赋值给实例属性self.name
        self.age = age  # 实例属性的名称和局部属性的名称可以相同

    # 实例方法
    # 定义在类中的函数称为方法，自带一个参数self
    def show(self):
        print(f"我叫{self.name},我今年{self.age}")  # 这里不能写xm，因为xm是一个局部变量，出了__init__之后无法使用，所以要用实例属性self.name，实例属性可以在整个类中使用

    # 静态方法
    @staticmethod
    def sm():
        print("这是一个静态方法，不能调用实例属性，也不能调用实例方法")

    # 类方法
    @classmethod
    def cm(cls):  # cls-->class的简写
        print("这是一个类方法，不能调用实例属性，也不能调用实例方法")


# 创建类的对象

stu = Student("wxl", 18)  # 为什么传入两个参数，因为__init__方法中，有两个形参，self，是自带的参数，无需手动输入

# 实例参数，使用对象名进行打点调用
print(stu.name, stu.age)

# 类属性，直接使用类名，打点调用
print(Student.school)

# 实例方法，使用对象名进行打点调用
stu.show()

# 类方法，@classmethod进行修饰的方法，直接使用类名打点调用
Student.cm()

# 静态方法，@staticmethod进行修饰的方法，直接使用类名打点调用
Student.sm()



"""
类方法，类属性，静态属性都是使用类名进行调用的
和实例有关的都是使用对象名去进行打点调用
"""