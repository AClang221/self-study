"""
https://codeforces.com/problemset/problem/1304/C
"""


def cz():
    n, m = map(int, input().split())
    a, b, tm = m, m, 0
    ans = "YES"
    for i in range(n):
        t, l, h = map(int, input().split())
        a -= (t - tm)
        b += (t - tm)
        tm = t
        a,b = max(a, l),min(b, h)
        if a > b:
            ans = "NO"
    return ans


for _ in range(int(input())):
    print(cz())
