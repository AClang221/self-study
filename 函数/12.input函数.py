# input函数的应用

# input 作用:接受来自用户的输入，返回值为str型
# 基本用法       变量 = input（“问题”）

present = input("你想要什么生日礼物")
print(present, type(present))

# input函数数据相加方法
# 1.
a = input("请输入一个数")
b = input("请输入例外一个加数")
print(type(a), type(b))
print(int(a)+int(b))
#  2.
a1 = int(input("请输入一个数"))
b1 = int(input("请输入例外一个加数"))
print(type(a1), type(b1))
print(a1+b1)
#  3.
a2 = input("请输入一个数")
a2 = int(a2)
b2 = input("请输入例外一个加数")
b2 = int(b2)
print(type(a2), type(b2))
print(int(a2)+int(b2))
