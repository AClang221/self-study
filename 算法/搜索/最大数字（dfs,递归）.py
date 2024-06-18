"""
https://www.lanqiao.cn/problems/2193/learning/
"""
N,A,B=map(int,input().split())
ans=0
grid=[int(i) for i in str(N)]
def dfs(i,ret,a,b):
    global ans
    if i<len(grid):
        x=grid[i]
        d=min(a,9-x)
        dfs(i+1,ret*10+x+d,a-d,b)
        if b>=x+1:
            dfs(i+1,ret*10+9,a,b-x-1)
    else:
        ans=max(ans,ret)
dfs(0,0,A,B)
print(ans)