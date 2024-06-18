scores = {"张三": 20, "李四": 50, "王五": 80, "老六": 60}
# 获取所有的key
keys = scores.keys()
print(keys, type(keys))
print(list(keys))  # 将所有key组成的视图转换成列表

# 获取所有的Value
Values = scores.values()
print(Values, type(Values))
print(list(Values))

# 获取所有的keys-Value
items = scores.items()
print(items, type(items))
print(list(items))  # 转换后的列表元素是由元组，组成的
