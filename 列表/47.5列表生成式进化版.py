"""列表生成式进化版"""
lst =[[float(i) for i in input().split()]for x in range(1, 10)]
"""
float(i) 定义列表中数据的类型
for i in input().split()  用于一行输入数据转化成列表
for x in range(1, 10)    用于判断输入的数据的行数
"""
print(lst)