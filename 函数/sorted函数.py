
"""
sorted函数使用方法
格式：sorted(可迭代类型，key=  ,reverse=)
key=   用来接收一个自定义的排序规则
reverse= 用来定义排序，默认为小到大，True为大到小，False为小到大
"""

a = [(2, "小黑"), (5, "小白"), (4, "张三"), (3, "王五")]
b=sorted(a,key=lambda x: x[0])
print(b)

