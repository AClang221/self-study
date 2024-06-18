"""
列表元素的删除操作放法：
1.remove（）一次删除一个元素
           重复元素只删除第一个
           元素不存在抛出ValueError
2.pop（）删除一个指定索引位置上的元素
        指定索引不存在抛出IndexError
        不存在索引值时，删除列表最后一个元素
3.切片    一次至少删除一个元素
4.clear（）清空列表
5.del   删除列表
"""

lst = [20, 10, 30, 10, 50]
print("--------remove操作----------")
print("操作前", lst)
lst.remove(10)
print("lst.remove(10)操作", lst, "重复元素只删除第一个")
lst.remove(20)
print("lst.remove(20)操作", lst, "一次删除一个元素")
# lst.remove(1000)   元素不存在抛出ValueError
print("--------pop操作---------------")
lst1 = [20, 10, 30, 10, 50]
print(lst1)
lst1.pop()
print("lst1.pop()操作", lst1, "不存在索引值时，删除列表最后一个元素")
lst1.pop(1)
print("lst1.pop(1)操作", lst1, "删除一个指定索引位置上的元素")
# lst.pop(10)  元素不存在抛出IndexError
print("-----------切片操作，删除至少一个元素，将产生一个新的列表对象----------------")
lst2 = [10, 20, 30, 40, 50]
new_lst = lst2[1:3]
print(lst2)
print(new_lst)
print("不产生新的内容，而是删除源列表中等内容")
lst2[0:2] = []
print(lst2)
print("---------clear操作------------")
lst3 = [10, 20, 30, 40, 50]
print(lst3)
lst3.clear()
print(lst3)
print("----------del操作-------")
del lst3
# print(lst3)   报错因为lst3列表被删除，无法打印
