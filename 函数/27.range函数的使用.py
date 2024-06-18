# range函数，用于生成一个（整数）序列
"""
优点：
不管range对象表示的整数序列有多长，所有的range对象占用的内存大小都是相同的，因为仅仅只要存取start，stop，step，
只有当用到range函数时，才会去计算序列中的相关元素
"""
"""
创建range函数的三种方式
1.range(stop) ------> 创建一个[0,stop)之间的整数序列，步长为 1
2.range(start，stop) ------> 创建一个[start,stop)之间的整数序，列步长为 1
3.range（start，stop，step） ------> 创建一个[start,stop)之间的整数序列，步长为 step
"""
r = range(10)
print(r)  # range函数，返回值是一个迭代器对象
print(list(r))  # 用于查看range对象中的整数序列   ----->list是列表的意思

# 判断指定的整数，在序列中是否存在    用  in 或 not in 进行判断

# in
print(5 in r)  # True 因为 5 在序列中
print(11 in r)  # False 因为 11 不在序列中
# not in
print(5 not in r)  # False 因为 5 在序列中
print(11 not in r)  # True 因为 11 不在序列中
