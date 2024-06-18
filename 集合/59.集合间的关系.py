"""两个集合是否相等（元素相同，集合相等）"""
s = {10, 20, 30, 40}
t = {30, 20, 10, 40}
print(s == t)  # True
print(s != t)  # False

"""一个集合是否是例一个集合的子集"""
s1 = {1, 2, 3, 4, 5}
t1 = {1, 2, 3, 4}
n = {100, 200}
print(s1.issubset(t1))  # s1是t1的子集吗，False
print(t1.issubset(s1))  # t1是s1的子集吗，True

"""一个集合是否是例一个集合的超集"""
print(s1.issuperset(t1))  # s1是t1的超集吗，True
print(t1.issuperset(s1))  # t1是s1的超集吗，False

"""两个集合是否（（（（没））））有交集"""
print(s1.isdisjoint(t1))  # False
print(s1.isdisjoint(n))  # True