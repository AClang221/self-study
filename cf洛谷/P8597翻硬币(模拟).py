# 输入数据s,r分别为初始和目标
s=str(input())
r=str(input())
lst_s=[str(i) for i in s]
lst_r=[str(i) for i in r]
ans=0
# 遍历元素，因为每次可以翻相邻两个，那么遍历（x-1）这个硬币状态要是不同，则翻第x-1与第x个硬币
for i in range(1,len(s)):
    if lst_s[i-1]!=lst_r[i-1]:
        ans+=1
        if lst_s[i]=="*":
            lst_s[i]="o"
        else:
            lst_s[i]="*"
print(ans)