"""
月饼是中国人在中秋佳节时吃的一种传统食品，不同地区有许多不同风味的月饼。
现给定所有种类月饼的库存量、总售价、以及市场的最大需求量，请你计算可以获得的最大收益是多少。
注意：销售时允许取出一部分库存。样例给出的情形是这样的：假如我们有 3 种月饼，
其库存量分别为 18、15、10 万吨，总售价分别为 75、72、45 亿元。
如果市场的最大需求量只有 20 万吨，那么我们最大收益策略应该是卖出全部 15 万吨第 2 种月饼、以及 5 万吨第 3 种月饼，
获得 72 + 45/2 = 94.5（亿元）。
输入格式：
每个输入包含一个测试用例。每个测试用例先给出一个不超过 1000 的正整数 N 表示月饼的种类数、
以及不超过 500（以万吨为单位）的正整数 D 表示市场最大需求量。
随后一行给出 N 个正数表示每种月饼的库存量（以万吨为单位）；
最后一行给出 N 个正数表示每种月饼的总售价（以亿元为单位）。数字间以空格分隔。
输出格式：
对每组测试用例，在一行中输出最大收益，以亿元为单位并精确到小数点后 2 位。
输入样例：
3 20
18 15 10    浮点型
75 72 45     浮点型
输出样例：
94.50
"""

N, D = map(int, input().split())  # N表示种类，D表示最大需求
Library_Stock = list(map(float, input().split()))  # 表示每种月饼的数量
total = list(map(float, input().split()))  # 表示每种月饼的总价
unit_price = []  # 表示月饼的单价
earnings = 0  # 表示月饼的收益
for i in range(N):
    unit_price.append(total[i]/Library_Stock[i])
max_price = max(unit_price)
max_price_location = unit_price.index(max_price)
while D != 0:
    if D >= sum(Library_Stock):
        print("%.2f" % sum(total), end="")
        D = 0
    elif D <= Library_Stock[max_price_location]:
        earnings = earnings+D*max_price
        print("%.2f" % earnings, end="")
        D = 0
    else:
        earnings += total[max_price_location]
        D -= Library_Stock[max_price_location]
        unit_price[max_price_location] = 0
        max_price = max(unit_price)
        max_price_location = unit_price.index(max_price)
