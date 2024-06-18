"""
可迭代对象有哪些：
a) 集合数据类型，如list、tuple、dict、set、str等
b) 生成器(generator)，包括生成器和带yield的生成器函数(generator function)
"""
"""
sorted(iter)            对可迭代对象进行排序

reversed(sequence)      反转序列生成新的迭代器对象

zip(iter1,iter2)        将iter1和iter2打包成元组并返回一个可迭代的zip对象

enumerate(iter)         根据iter对象创建一个enumerate对象

all(iter)               判断可迭代对象iter中所有元素的布尔值是否为True，全为True则True否则为False

any(iter)               判断可迭代对象iter中所有元素的布尔值是否为False，一个为True则True，都为False则False

next(iter)              判断迭代器的下一个元素

filter(function,iter)   通过指定条件过滤序列并返回一个迭代器对象

map(function,iter)      通过函数function对可迭代对象iter的操作返回一个迭代器对象
"""

lst = [56, 52, 23, 65, 45, 75]
# sorted函数的使用
sorted_lst = sorted(lst)  # 默认为升序,False
print(sorted_lst)

# reversed函数的使用
reversed_lst = reversed(lst)
print(reversed_lst)  # 结果是一个迭代器对象
print(list(reversed_lst))

# zip函数的使用,当两个可迭代对象长度不一致时按照短的来
x = ["a", "b", "c", "d"]
y = [12, 34, 435, 654, 76, 5]
zip_lst = zip(x, y)
print(zip_lst)
print(list(zip_lst))

# enumerate函数的使用
enumerate_lst = enumerate(lst, start=1)
print(enumerate_lst)
print(list(enumerate_lst))

# all函数的使用
lst2 = [10, 203, 23, ""]
print(all(lst2))  # 结果为False因为空字符串布尔值为False
print(all(lst))

# any函数的使用
lst3 = ["", "", "", ""]
print(any(lst3))

# next函数的使用
a_zip = zip(x, y)  # a_zip相当于是一个为解包的迭代对象，通过next函数可以将其内容依次取出
print(next(a_zip))
print(next(a_zip))
print(next(a_zip))
print(next(a_zip))


def fun(num):
    return num % 2 == 1  # 结果可能为True也可能为False


# filter函数的使用
ans = filter(fun, range(10))  # 将range产生的数放到fun函数中进行判断，并将产生的值放入一个新的容器中
print(list(ans))


def upper(x):
    return x.upper()


lst4 = ["hello", "world", "python"]
# map函数的使用
ans1 = map(upper, lst4)
print(list(ans1))

"""
map与filter的区别在于，filter用来筛选，而map不进行判断
"""