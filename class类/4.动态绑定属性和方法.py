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


# 创建两个Student类型的对象
stu = Student("z", 12)
stu1 = Student("y", 13)
print(stu.name, stu.age)
print(stu1.name, stu1.age)

# 为stu1动态绑定一个实例属性
stu1.gender = "boy"
print(stu1.name, stu1.age, stu1.gender)


# 动态绑定方法
def introduce():
    print("我是一个普通的函数，我被动态绑定成了stu1对象的方法")


stu1.fun = introduce  # 函数的赋值操作
stu1.fun()