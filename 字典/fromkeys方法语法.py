"""
Python 字典 fromkeys() 函数用于创建一个新字典，
以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。

格式： dict.fromkeys(seq,value)

参数：
seq -- 字典键值列表。
value -- 可选参数, 设置键序列（seq）对应的值，默认为 None。
"""
lst = ["name", "vge", "sex"]
ans = dict.fromkeys(lst, 20)
print(ans)
