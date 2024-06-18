# 列表的创建方式
"""
1.使用中括号
表达方式
列表对象名 = [内容， 内容， 内容]
"""
lst1 = ["hello", "world"]
print(id(lst1), type(lst1), lst1)

"""2.使用内置函数list（）"""
lst2 = list(["hello", "world", 2])
print(id(lst2), type(lst2), lst2)
