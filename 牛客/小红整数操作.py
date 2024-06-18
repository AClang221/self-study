"""
链接：https://ac.nowcoder.com/acm/contest/73760/D
来源：牛客网
小红拿到了两个正整数x,y，她可以进行以下两种操作：
1. 将两个数同时乘以a。
2. 若a既是x的因子，也是y的因子，则将两个数同时除以a。
小红希望最终两个数都在[l,r]区间内。她想知道最终的
x有多少种不同的取值方案？
"""

import math

x, y, l, r = map(int, input().split(" "))

tt = math.gcd(x, y)

x //= tt
y //= tt

end = min(r // x, r // y)
start = max((l + x - 1) // x, (l + y - 1) // y)
print(max(end - start + 1, 0))

