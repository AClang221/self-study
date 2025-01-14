"""
Python 字典 copy() 函数返回一个字典的浅复制。

格式：dict.copy()

参数：没有
"""
dict1 = {'user': 'ru noob', 'num': [1, 2, 3]}

dict2 = dict1  # 浅拷贝: 引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象是引用

# 修改 data 数据
dict1['user'] = 'root'
dict1['num'].remove(1)

# 输出结果
print(dict1)  # {'user': 'root', 'num': [2, 3]}
print(dict2)  # {'user': 'root', 'num': [2, 3]}
print(dict3)  # {'user': 'ru noob', 'num': [2, 3]}

"""
总结：不用copy改变其中之一两个会一起变，
使用copy改变键时不会一起改变，改变值时会一起改变
"""