"""
1.封装：   权限的控制：是通过对属性或方法添加下划线，双下划线，以及首位双下划线来实现
        单下划线开头：以单下划线开头的属性或方法表示protected受保护的成员，这类成员被视为仅供内部使用，
                    允许类本身和子类进行访问，但实际上它可以被外部代码访问
        双下划线开头：表示private私有的成员，这类成员只允许定义该属性或方法的类本身进行访问
        首尾双下划线：一般表示特殊的方法
"""


class Student:
    def __init__(self, name, age, gender):
        self._name = name                   # self._name受保护只能本类和子类访问
        self.__age = age                    # self.__age表示私有的，只能类本身进行访问
        self.gender = gender                # 普通实例属性，类的内部外部和子类都可以进行访问

    def _fun1(self):    # 受保护的
        print("子类及本身可访问")

    def __fun2(self):   # 私有的
        print("只有定义的类可访问")

    def show(self):     # 普通的实例方法
        self._fun1()    # 类本身访问受保护的实例方法
        self.__fun2()   # 类本身访问私有方法
        print(self._name)   # 受保护的实例属性
        print(self.__age)   # 私有的实例属性


# 创建一个学生类的对象
stu = Student("wxl", 18, "男")
# 类的外部
print(stu._name)
# print(stu.__age)      AttributeError: 'Student' object has no attribute '__age'

# 调用受保护的实例方法
stu._fun1()     # 子类及本身可以访问
# 私有方法
# stu.__fun2()  # AttributeError: 'Student' object has no attribute '__fun2'
# 私有实例属性和方法访问方式
print(stu._Student__age)
stu._Student__fun2()            # 不推荐这么使用

print(dir(stu))
