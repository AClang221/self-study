"""
count() 方法用于统计字符串里某个字符或子字符串出现的次数。
可选参数为在字符串搜索的开始与结束位置
"""

""" 
例如:
给定一个由小写字母构成的字符串。
请你计算，字符 'a' 在字符串中出现了多少次
"""

text = str(input())
print(text.count("a",0,len(text)))

"""
str.count(sub, start= 0,end=len(string))
此处:
str——————表示的是要进行查询的文本
sub——————表示的是要进行查询的字符
"""