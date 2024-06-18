"""
lambda函数，又称匿名函数，用来编写简单的函数,这种函数只能用一次
格式：函数名=lambda 形参：要实现的作用
"""

Sum_lambda = lambda a,b: a+b
a,b=map(int,input().split())
print(Sum_lambda(a,b))
print("-"*30)
lst = [10,20,30,40,50,60]
for i in range(len(lst)):
    ans=lambda x : x[i]
    print(ans(lst))