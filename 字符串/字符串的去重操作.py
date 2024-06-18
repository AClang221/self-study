s = "hhheeelllooowww"
# 方法一：直接for语句进行遍历
new_s = ""
for i in s:
    if i not in new_s:
        new_s += i  # 直接使用+进行字符串拼接
print(new_s)

# 方法二：使用字符串的索引进行遍历
new_s2 = ""
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2 += s[i]
print(new_s2)

# 通过集合去重+列表排序
new_s3=set(s)
print(new_s3)
lst=list(new_s3)
lst.sort(key=s.index)
print("".join(lst))
