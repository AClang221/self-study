class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gander = gender  # self.__gander 是私有的实例属性

    # 使用装饰器@property 修改方法，将方法转换成属性使用
    @property           # 方法转换成属性后，只能查看值，不能修改值
    def gender(self):
        return self.__gander

    # 将gender这个属性设置为可写属性
    @gender.setter
    def gender(self, value):
        if value != "男" and value != "女":
            print("性别有误，已将性别设置为男")
            self.__gander = "男"
        else:
            self.__gander = value


stu = Student("kare", "男")
print(stu.name, "的性别是：", stu.gender)


stu.gender = "其他"                           # 这里的gender是赋值操作，进行的是12行的代码
print(stu.name, "kare的性别是", stu.gender)    # 这里的gender是取值操作，进行的是8行代码
