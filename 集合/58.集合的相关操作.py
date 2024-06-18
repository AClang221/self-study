s = {1, 2, 3, 50}
"""集合元素的判断操作"""
print(1 in s)
print(10 in s)
print(10 not in s)
print(1 not in s)

"""集合元素的新增操作"""
s.add(80)  # 使用add进行添加，一次添加一个元素
print(s)
s.update({200, 400, 300})  # 使用update进行添加,一次至少添加一个元素，添加到形式多样化,添加重复元素时只会添加一个
s.update((500, 600))
s.update([700, 800])
print(s)

t = {1, 2, 3, 4, 5, 6, 7, 8}
print("------------------------------------------------")
"""集合元素的删除操作"""
t.remove(1)  # remove一次删除一个元素，要是元素不存在抛出KeyError
print(t)
t.discard(9)  # discard一次删除一个元素，要是元素不存在不抛出异常
print(t, "不存在不抛出异常")
t.pop()  # 一次删除任意一个元素，不能给参数，给参数会报错
print(t)
t.clear()  # 清空集合
print(t)
