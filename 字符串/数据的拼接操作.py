"""
字符串拼接的几种方法：
        1.使用str.join()方法进行拼接字符串
        2.直接拼接
        3.使用格式化字符串进行拼接
"""
s1="hello"
s2="world"

# 使用+进行拼接
print(s1+s2)

# 使用字符串的join()方法
print(" ".join([s1,s2]))  # join前为空格表示用空格连接
print("!!!!".join([s1,s2]))

# 直接拼接
print("hello""world")

# 使用格式化字符串进行拼接
pass
