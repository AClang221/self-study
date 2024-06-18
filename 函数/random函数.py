"""
random.randint(start,stop)用于生成一个随机数
start -- 必需， 一个整数，指定开始值
stop -- 必需， 一个整数，指定结束值
这个范围包括两个必需值
"""
import random

for i in range(20):
    a = random.randint(1, 10)
    print(a)
