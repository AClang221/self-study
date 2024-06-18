"""
列表元素排列操作：
1.调用sort（）方法默认排列方式从小到大
           可以指定reverse=True进行降序排列
2.调用内置函数sorted（）
            可以指定reverse=True进行降序排列
            原列表不发生改变，产生新的一个列表
"""

lst = [10, 50, 30, 90, 100]
print("排序前的列表", lst, id(lst))
# 开始排序，调用列表对象的的sort（）方法，升序排列
lst.sort()
print("排序后列表", lst, id(lst))
# 通过指定关键字降序排列
lst.sort(reverse=True)
print(lst)
# 通过指定关键字升序排列
lst.sort(reverse=False)
print(lst)

print("-------------------使用用内置函数sorted（），产生一个新的列表对象--------------")
lst1 = [20, 50, 10, 90, 40]
print("原列表", lst1)
# 开始排序
new_lst1 = sorted(lst1)
print("操作后源列表不发生改变", lst1)
print("操作后", new_lst1)
# 指定关键参数，降序排列
jiang_lst = sorted(lst1, reverse=True)
print(jiang_lst)
