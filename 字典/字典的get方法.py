"""
dict.get(key ,value)
Key-----字典中要查找的键
value-----可选，如果指定键的值不存在时，返回该默认值，默认值为None，存在则返回存在的值
"""
lst = ["a", "b", "c", "a", "b", "c"]
dic = {}
for i in lst:
    dic[i] = dic.get(i, 0)+1
print(dic)


"""补充说明字典中的查询，增删改都是0(1),not in操作查的是键"""