"""
列表的特点
1.列表元素按顺序有序排列
2.任意类型数据混存
3.索引映射唯一个数据

索引    -5        -4       -3      -2       -1
数据  "hello"   "world"   123      123    "你好"
索引    0          1       2       3        4
"""
# 索引的用法
lst1 = ["hello", "world", 123, 123, "你好"]
print(lst1[0])
print(lst1[-5])
"""4.列表可以存储重复数据"""
print(lst1[3])
print(lst1[4])
"""5.根据需要动态分配和回收内存"""
