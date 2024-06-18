"""
https://codeforces.com/contest/1956/problem/A
"""

def daan(ans):
    while True:
        zt = 1
        t = 0
        for i in sc:
            if i <= ans:
                t += 1
                zt=0
            else:
                break
        if zt:
            return ans
        ans -= t


def cz():
    global sc
    k, q = map(int, input().split())
    sc = [i for i in map(int, input().split())]
    lst = [i for i in map(int, input().split())]
    ans = []
    while lst:
        mub = lst.pop(0)

        ans.append(daan(mub))
    return ans


for i in range(int(input())):
    for i in cz():
        print(i, end=" ")
    print()
