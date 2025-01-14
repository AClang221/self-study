def fun(a,b,c):  # a,b,c在函数的定义处，所以是形式参数
    print("a=",a)
    print("b=", b)
    print("c=", c)

# 函数的调用
fun(10,20,30)  # 函数调用时的参数传递，称为位置传参
lst = [11,22,33]
fun(*lst)  # 在函数调用时，将列表中的每个元素都转换为位置实参传入
print("---------------")
fun(a=100,b=200,c=300) # 函数的调用，所以是关键字实参

dic = {"a" : 111, "b" : 222, "c" : 333}
fun(**dic) # 在函数调入时，将字典中的键值对都转换为关键字实参传入