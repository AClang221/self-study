"""
大小写转换
1.upper()   把字符串中所有字符转换成 （大） 写字母
2.lower()   把字符串中所有字符转换成 （小） 写字母
3.swapcase()   把字符串中所有大写字母转换成 （小） 写字母，所有小写字母转换成 （大） 写字母
4.capitalize()   把第一个字符转换成大写字母，其余都转换成小写字母
5.title()   把每一个单词的第一个字母转换成大写字母，其余都转换成小写字母
"""
s = "hello,python"
a = s.upper()  # 转换成大写之后，会产生一个新的字符串对象，因为字符串是不可变对象
print(s, id(s), "原来的")
print(a, id(a), "转大写后的")
b = s.lower()  # 转换后内容一样，但是是新的字符串
print(b, id(b), "转小写后的")
print("----------------------------------------------------------------------")
s1 = "Hello,pYThon"
c = s1.swapcase()
print(s1, id(s1), "原来的")
print(c, id(c), "大小互换后的")
d = s1.capitalize()
print(d, id(d))
e = s1.title()
print(e, id(e))
