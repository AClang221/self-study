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


# 根据模板可以创建出N多个对象
stu = Student("z", 18)
stu1 = Student("c", 18)
stu2 = Student("x", 18)  # =右边都是Student

print(type(stu))
print(type(stu1))
print(type(stu2))

Student.school = "浙江经济职业技术学院"  # 给类的属性赋值

# 将学生对象存储到列表中
lst = [stu, stu1, stu2]  # 列表中的元素是Student类型的对象
for item in lst:  # item是列表中的元素，是Student类型的对象
    item.show()  # 对象名打点调用实例方法
