'''https://www.lanqiao.cn/problems/1591/learning/'''


fw=1414206
a = [0] * fw
b = [0] * fw
for i in range(1, fw ):
    a[i] = i + a[i - 1]
    b[i] = a[i] + b[i - 1]

def Find(x):
    l,r=0,1414206
    while l<r:
        mid=(l+r+1)//2
        if x>=a[mid]:
            l=mid
        else:
            r=mid-1
    return b[l]+a[x-a[l]]

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(Find(r)-Find(l-1))