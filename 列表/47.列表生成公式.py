"""
生成列表的公式
语法格式：  [i*i for i in range(1,10)]
        i*i -------> 表示列表元素的表达式
        i---------->  自定义变量
        range（）--------->  可迭代对象
注意事项:“表示列表元素的表达式”，中通常包含自定义变量
"""
lst = [i for i in range(1, 10)]
print(lst)
lst1 = [i * i for i in range(1, 10)]
print(lst1)

"""列表中的元素为2，4，6，8，10"""
lst2 = [i * 2 for i in range(1, 6)]
print(lst2)

