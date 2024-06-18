"""
将字符串中的字符进行替换
因为Python中的字符串是「不可变」的，所以 replace() 不会改变原字符串的内容，而是返回一个新的字符串。
string.replace(old,new,count)
old ：（必选，字符串类型）被替换的字符串
new ：（必选，字符串类型）替换后的字符串
count ：（可选，整型）替换的次数
"""
str1="hello hello hello hello"
str2=str1.replace("hello","world")
str3=str1.replace("hello","world",1)
print(str2)
print(str3)