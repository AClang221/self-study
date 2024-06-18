"""index()"""
lst1 = ["hello", "world", 123, 123, "你好"]
# index    0        1       2    3     4
print(lst1.index(123))  # 1.如查列表中存在N个相同元素，只会返回相同元素的第一个索引值

# 2.如果查询的元素在列表中不存在，则会抛出ValueError
print(lst1.index(1233))  # 输出ValueError，因为1233不存在于列表中

# 3.还可以在指定的start和stop之间进行查找
print(lst1.index("hello", 1, 5))  # 输出ValueError，因为hello不在索引1-5之间
