"""
字符串的编码：
        将str类型转换成bytes类型，需要使用到字符串的encode（）方法
    语法格式：   str.encode(encoding= 'utf-8' , errors = 'strict/ignore/replace')
    utf-8 为编码格式
    errors 表示编码出错时的解决方案
            strict 为严格的要是编码编不过来时会报错
            ignore 为忽略编码编不过来时会跳过忽略
            replace  当编码编不过来时会用  ？  代替


字符串的解码：
        将bytes类型转换成str类型，需要使用到bytes类型的decode方法
    语法格式：   bytes.decode(需要被解码的东西, encoding= 'utf-8' , errors = 'strict/ignore/replace')
"""

# 编码过程
s="伟大的中国梦"
code_utf=s.encode(encoding="utf-8")
print(code_utf)  # utf-8中，英文占一个字节，中文占三个字节
code_gbk=s.encode(encoding="gbk")
print(code_gbk)  # gbk,中文两个字节英文一个字节

# 解码过程
print(bytes.decode(code_utf,encoding="utf-8"))
print(bytes.decode(code_gbk,encoding="gbk"))