"""
1.占位符：
    %d：表示十进制整数格式
    %s：字符串格式
    %f：浮点数格式

2、f-string
    用{}标明被替换的字符

3.str.format()
    详细格式：
        : 引导符号
        填充   用于填充单个字符
        对齐方式  <左对齐   >右对齐  ^居中对齐
                字符串默认左对齐，数值型默认右对齐
        宽度   字符串的输出宽度
        ，    数字的千位分隔符
        .精度   浮点数小数部分的精度或字符串的最长输出长度
        类型   整数类型b\d\o\x\X,大小x都为16进制
              浮点数类型e\E\f\%
"""

name = "abc"
age = 18
score = 98
print("姓名：%s，年龄：%d，成绩：%d"%(name,age,score))

print(f"姓名：{name},年龄：{age}，成绩：{score}")

print("姓名：{0},年龄：{1}，成绩：{2}".format(name,age,score))


print("{0:*<20}".format("helloword"))  # 填充为*  左对齐  宽度为20
print("{0:*^20}".format("helloword"))  # 填充为*  居中对齐  宽度为20
print("{0:,.3f}".format(1234567890.123456))  # 分隔符三位一隔，.3f表示保留三位小数

# 类型
s=20
print("二进制：{0:b}, 八进制；{0:o}, 十进制：{0:d}, 十六进制：{0:x}".format(s))  # 表示输出2，8，10，16进制
nub = 3.1415926
print("{0:.2f},{0:.2e},{0:.2E},{0:.2%}".format(nub))
