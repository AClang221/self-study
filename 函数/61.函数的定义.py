def calc(a,b):  # a,b称为（形式参数），简称（形参）， 形参在定义处
    c = a+b
    return c


result=calc(10,20)  # 10,20称为（实际参数的值），简称（实参），实参的位置是函数的调用处
print(result)


res=calc(b=10,a=20)  #  等号左边的变量名称称为————关键字参数
print(res)


"""实参和形参可以不相同"""
"""
当写函数调用时因写成
函数名（）
当要将函数作为参数作为值时
函数名
"""