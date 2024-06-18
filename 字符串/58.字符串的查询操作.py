s = "hello,hello"
print(s.index("lo"))  # 查找字符串中lo，（第一次）出现的位置
print(s.rindex("lo"))  # 查找字符串中lo，（最后一次）出现的位置
print(s.find("lo"))  # 查找字符串中lo，（第一次）出现的位置
print(s.rfind("lo"))  # 查找字符串中lo，（最后一次）出现的位置

# print(s.index("k")) 不存在抛出异常  ValueError: substring not found
# print(s.rindex("k")) 不存在抛出异常  ValueError: substring not found
print(s.find("k"))  # 不存在时为  -1
print(s.rfind("k"))  # 不存在时为  -1
