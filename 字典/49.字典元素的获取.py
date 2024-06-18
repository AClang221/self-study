"""
字典元素的获取放法：
"""

"""1.使用[]"""
scores = {"张三": 40, "李四": 20, "王五": 60}
print(scores["张三"])
# print(scores["柽柳"])   报错KeyError
"""2.使用get()方法"""
print(scores.get("张三"))
print(scores.get("柽柳"))  # 输出None，不会报错
print(scores.get("麻雀", 90))  # 90在查找“麻雀”所对的Value不存在时，提供一个默认值

"""2.使用values"""
for i in scores.values():
    print(i,end=" ")