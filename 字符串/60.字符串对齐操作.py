"""
字符串对齐方式
1.center():居中对齐，第一个参数指定宽度，第二个参数指定填充符（可选，默认为空格），如果设置宽度小于原字符串宽度，则返回原来字符串
2.ljust():左对齐，第一个参数指定宽度，第二个参数指定填充符（可选，默认为空格），如果设置宽度小于原字符串宽度，则返回原来字符串
3.rjust():右对齐，第一个参数指定宽度，第二个参数指定填充符（可选，默认为空格），如果设置宽度小于原字符串宽度，则返回原来字符串
4.zfill():右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串的宽度，如果设置宽度小于等于原字符串宽度，则返回原来字符串
"""

s = "hello,python"
"""居中对齐"""
print(s.center(20, "*"))
print(s.center(20))
print(s.center(10, "*"))
print("----------------------------")
"""左对齐"""
print(s.ljust(20, "*"))
print(s.ljust(20))
print(s.ljust(10, "*"))
print("------------------------------")
"""右对齐"""
print(s.rjust(20, "*"))
print(s.rjust(20))
print(s.rjust(10, "*"))
print("-123".rjust(20, "0"))
print("-------------------------------")
"""右对齐，默认0填充"""
print(s.zfill(20))
print(s.zfill(10))
print("-123".zfill(20))
