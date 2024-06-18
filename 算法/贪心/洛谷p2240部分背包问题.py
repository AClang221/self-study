"""
阿里巴巴走进了装满宝藏的藏宝洞。藏宝洞里面有N堆金币，第i堆金币重量和价值分别为
mi,vi，有一个能装T重量的背包，尽可能拿最多价值的金币
输入格式：
        第一行两个整数 N，T
        接下来N行，每行两个整数mi，vi
输出格式：
        一个实数表示答案，输出保留两位小数
"""

N, T = map(int, input().split())
lst = [[i for i in map(float, input().split())] for y in range(N)]
for i in range(N):
    price = float(lst[i][1] / lst[i][0])
    lst[i].append(price)
price_lst = sorted(lst, key=lambda x: x[2], reverse=True)
total = 0

all_weight = 0
for i in range(N):
    all_weight += lst[i][0]
i = 0
if T > all_weight:
    for i in range(N):
        total += lst[i][1]
else:
    while T > 0:
        if T > price_lst[i][0]:
            T -= price_lst[i][0]
            total += price_lst[i][1]
        else:
            total += price_lst[i][2] * T
            break
        i += 1

print("%.2f" % total)