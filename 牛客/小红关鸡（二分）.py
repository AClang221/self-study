'''
https://ac.nowcoder.com/acm/contest/76133/C
'''
n,k=map(int,input().split())
lst=[i for i in map(int,input().split())]
lst.sort(reverse=False)
if k+2>=lst[n-1]-lst[0]+1:
    print(1)
else:
    ans=0
    total=0
    i=0
    left = lst[i]
    right = left + k+1
    while True:
        if right>lst[n-1]:
            break
        for t in range(left,right+1):
            if t in lst:
                ans+=1
        total=max(total,ans)
        i+=1
        ans-=1
        left = right+1
        right = lst[i] + k+1
    print("%.4f"%(total/n))
