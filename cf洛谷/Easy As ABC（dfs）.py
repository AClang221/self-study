"""https://codeforces.com/problemset/problem/1906/A"""


def dfs(x,y):
    global ans,Min_ans
    ans+=graph[x][y]
    if len(ans)==3:
        Min_ans=min(Min_ans,ans)
    else:
        for fx,fy in f:
            nx=fx+x
            ny=fy+y
            if 0<=nx<3 and 0<=ny<3 and is_graph[nx][ny] and len(ans)<=2:
                is_graph[nx][ny]=0
                dfs(nx,ny)
                is_graph[nx][ny]=1
                ans=ans[:len(ans)-1]


graph=[]
for i in range(3):
    graph.append(str(input()))
f=[(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]
is_graph=[[ 1 for i in range(3)]for j in range(3)]
Min_ans="ccc"
fir="C"
for i in range(3):
    for j in range(3):
        if fir >=graph[i][j]:
            ans = ""

            is_graph[i][j] = 0
            dfs(i, j)
            is_graph[i][j]=1
            fir=graph[i][j]
print(Min_ans)