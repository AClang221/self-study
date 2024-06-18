"""
功能：定义类，作用是指向下一个节点
"""


class Node:
    def __init__(self, elem):  # 创建链表
        self.elem = elem
        self.next = None  # 初始设置下一个节点为空


"""
功能：创建学生节点类
"""


class Student:
    def __init__(self):
        self.name = ""
        self.sex = ""
        self.next = None


head = Student()                            # 建立链表头部
head.next = None                            # 下一个元素为空
prt = head                                  # 存储指针的位置
select = 0                                  # 用来选择
while select != 2:
    print("(1）添加   (2)退出程序")            # 提示
    select = int(input("请输入一个选项："))
    if select == 1:                         # 选择1时，添加信息
        NewData = Student()                 # 添加下一个元素
        NewData.no = input("学号：")         # 添加学号
        NewData.name = input("姓名：")       # 添加姓名
        NewData.sex = input("性别：")        # 添加性别
        prt.next = NewData                  # 存储指针设置为新元素所在位置
        NewData.next = None                 # 下一个元素的next先设置为空
        prt = prt.next                      # 选择下一个结点
    elif select == 2:
        break
    else:                                   # 选择其他时提示有误
        print("输入有误")
