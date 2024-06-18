"""
https://www.lanqiao.cn/problems/2191/learning/
"""
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
def cheek(mid):
    surplus=m
    for i in range(len(a)):
        if a[i]>=mid:continue
        if a[i]+b[i]<mid or mid>a[i]+surplus:
            return 0
        surplus=surplus-mid+a[i]
    return 1


left,right=0,2*n
while left<right:
    mid=(left+right+1)//2
    if cheek(mid):
        left = mid
    else:
        right = mid-1
    print(left,right,mid)
print(left)
