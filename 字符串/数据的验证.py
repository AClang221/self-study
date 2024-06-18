"""
str.isdigit()   所有字符都是数字（阿拉伯数字）
str.isnumeric() 所有字符都是数字
str.isalpha()   所有字符都是字母（包含中文字符）
str.isalnum()  所有字符都是数字或字母（包含中文字符）
str.islower()  所有字符都是小写
str.isupper()  所有字符都是大写                          中文既是大写又是小写
str.istitle()  所有字符都是首字母大写     不是首字母也大写了会报错，用空格将将个单词隔开的话两个单词首字母都要大写
str.isspace()  所有字符都是空白字符（\n,\t等）
"""

# str.isdigit()   所有字符都是数字（阿拉伯数字）
print("123".isdigit())  # True
print("ⅠⅡⅢⅣⅤⅥⅦⅧⅨ".isdigit())  # False
print("一二三".isdigit())  # False
print(" 壹贰叁".isdigit())  # False
print("0b1010".isdigit())  # False
print("-"*20)
# str.isnumeric() 所有字符都是数字
print("123".isnumeric())  # True
print("ⅠⅡⅢⅣⅤⅥⅦⅧⅨ".isnumeric())  # True
print("一二三".isnumeric())  # True
print("壹贰叁".isnumeric())  # True
print("0b1010".isnumeric())  # False
print("-"*20)
# str.isalpha()   所有字符都是字母（包含中文字符）
print("hello你好".isalpha())  # True
print("hello你好123".isalpha())  # False
print("hello你好一二三".isalpha())  # True
print("hello你好壹贰叁".isalpha())  # True
print("hello你好Ⅲ".isalpha())  # False
print("-"*20)
# str.isalnum()  所有字符都是数字或字母（包含中文字符）
print("hello你好".isalnum())  # True
print("hello你好123".isalnum())  # True
print("hello你好一二三".isalnum())  # True
print("hello你好壹贰叁".isalnum())  # True
print("hello你好Ⅲ".isalnum())  # True
print("hello你好Ⅲ".isalnum())  # True

