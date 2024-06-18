"""
列表元素增加操作方式：
1.append（）在列表的末尾添加一个元素       添加多个元素多个元素会被当成一个元素添加到列表
2.extend（）在列表的末尾至少添加一个元素    可以添加多个元素
3.insert（）在列表任意位置添加一个元素     添加多个元素多个元素会被当成一个元素添加到列表
4.切片      在列表任意位置至少添加一个元素   可以添加多个元素    会将原先的内容置换掉
"""

lst = [20, 30, 40, 50]
print("添加元素之前", lst, id(lst))
lst.append(60)
print("添加元素之后", lst, id(lst))
print("以上操作说明，添加操作不会生成新的列表")
lst2 = ["hello", 'world']
lst.append(lst2)
print(lst)
print("lst.append（lst2）操作将lst2作为一个元素添加到了lst中")
lst.extend(lst2)
print(lst)
print("使用extend将lst2内的元素分别添加到lst中")
lsn = [10, 20]
lsn.insert(0, 20)
print(lsn)
print("使用insert可以在列表任意位置插入一个元素")
lsn2 = ["hello", "wxl"]
lsn.insert(0, lsn2)
print(lsn)
print("使用lsn.insert(0,lsn2)操作将lsn2作为了一个元素添加到了lsn中")

print("----------切片操作-----------------------------------------")
lst3 = ["哈喽", "我的"]
print(lst)
lst[1:] = lst3
print(lst)
print("切片操作将指定索引后的内容进行了置换操作")
 