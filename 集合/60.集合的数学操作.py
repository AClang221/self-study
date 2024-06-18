s = {10, 20, 30, 40}
s1 = {20, 30, 40, 50, 60}

"""求两个集合的交集"""
print("交集")
print(s.intersection(s1))
print(s & s1)

"""求两个集合的并集"""
print("并集")
print(s.union(s1))
print(s | s1)

"""求两个集合的差集"""
print("差集")
print(s.difference(s1))  # 相当于s中的元素除去，s与s1的交集
print(s - s1)

"""求两个集合的对称差集"""
print("对称差集")
print(s.symmetric_difference(s1))  # 相当于s与s1中的元素，除去s与s1的交集
print(s ^ s1)
