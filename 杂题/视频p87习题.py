"""
题目：编写程序接受用户输入分数的信息
需求：如果分数在0-100之间，输出成绩。如果不在则抛出异常，提示分数必须在0-100之间
"""


try:
    nub=eval(input("请输入分数："))
    if 0<=nub<=100:
        print("你的分数是：",nub)
    else:
        raise Exception("分数必须在0-100之间")
except Exception as e:
    print(e)