"""
enumerate函数：
            这个函数的基本应用就是用来遍历一个集合对象，它在遍历的同时还可以得到当前元素的索引位置。
            可以改变元素索引值的默认大小
"""
lst = [10,20,30,40,50,60,70,80,90]
for i in range(len(lst)):
    print(f"索引值{i},值{lst[i]}")
print("-"*50)


for index,value in enumerate(lst,start=10):
    print(f"索引值{index}，值{value}")