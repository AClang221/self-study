"""
继承：     1.在python中一个子类可以继承N多个父类
          2.一个父亲也可以拥有N多个子类
          3.如果一个类没有继承任何类，那么这个类默认继承的是object类
继承语法结构：：
            class 类名（父类1，父类2，.....，父类N）
                pass
"""


class Person:       # 默认继承了object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"大家好我叫{self.name}，今年{self.age}岁")


# Student继承Person类
class Student(Person):
    # 编写初始化方法
    def __init__(self, name, age, stuno):
        super().__init__(name, age)  # 调用父类的初始化方法，为我们的nanme和age赋值
        self.stuno = stuno


# Doctor继承Person类
class Doctor(Person):
    # 编写初始化方法
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department


# 创建第一个子类对象
stu = Student("HBR", 18, 1001)
stu.show()
doctor = Doctor("Taigar", 16, "外科")
doctor.show()