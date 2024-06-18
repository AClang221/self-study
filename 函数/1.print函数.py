# 可以输出数字
print(25)

# 可以输出字符串
print("wad")

# 可以输出含有运算符的表达式
print(1+1)

# 可以输入到文件夹中，注意1.指定的盘符必须存在。2.必须以file= 的形式输出
a= open(r"E:\python题\text.txt",'a+')  # a+的意思：如果文件不存在那就创建，如果存在内容进行追加
print('hello,world', file=a)
a.close()

# 不进行换行输出
print("520", "1314", "you")
