# for in 的练习

# 题目：打印100-999之间的水仙花数

for item in range(100, 1000):
    ge = item % 10  # 个位
    shi = item // 10 % 10  # 十位
    bai = item // 100  # 百位
    if ge ** 3 + shi ** 3 + bai ** 3 == item:
        print(item)
