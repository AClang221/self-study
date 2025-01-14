"""
每种草药可以无限制地疯狂采摘
输入格式
    输入第一行有两个整数，分别代表总共能够用来采药的时间 t 和代表山洞里的草药的数目 m
    第 2到第(m+1)每行两个整数，第(i+1) 行的整数ai，bi分别表示采摘第i 种草药的时间和该草药的价值。
输出格式
    输出一行，这一行只包含一个整数，表示在规定的时间内，可以采到的草药的最大总价值。

示例
输入
70 3
71 100
69 1
1 2

输出
140
"""
t, m = map(int, input().split())
dp = [0] * (t+1)    # 一维数组用来保存当前容量下能装的最大价值
# 遍历每一件物品
for _ in range(m):
    a, b = map(int, input().split())    # a,b分别表示物品的重量和价值
    # 遍历背包
    for j in range(t,a-1,-1):
        dp[j] = max(dp[j], dp[j-a] + b)
# 输出结果
print(dp[t])