"""
题目描述   洛谷p1101
给一      n*n     的字母方阵，内可能蕴含多个 `yizhong` 单词。
单词在方阵中是沿着同一方向连续摆放的。
摆放可沿着 8个方向的任一方向，同一单词摆放时不再改变方向，单词与单词之间可以交叉，因此有可能共用字母。
输出时，将不是单词的字母用 `*` 代替，以突出显示单词。
输入格式
    第一行输入一个数  n
    第二行开始输入 n * n 的字母矩阵。
输出格式
    突出显示单词的 n * n 矩阵。
样例 #1
    样例输入 #1
```
7
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
```
样例输出 #1
```
*******
*******
*******
*******
*******
*******
*******
```
样例 #2
样例输入 #2
```
8
qyizhong
gydthkjy
nwidghji
orbzsfgz
hhgrhwth
zzzzzozo
iwdfrgng
yyyygggg
```
样例输出 #2
```
*yizhong
gy******
n*i*****
o**z****
h***h***
z****o**
i*****n*
y******g
```
"""

# 代码
n=int(input())                  # 表示矩阵的大小
res="yizhong"                   # 要进行寻找的目标
dx=[1,1,0,-1,-1,-1,0,1]         # 表示第x行
dy=[0,1,1,1,0,-1,-1,-1]         # 表示第y列
graph=[]                        # 表示的输入的数据的图
out=[[0,0]for i in range(7)]    # 用于存放当前判断位置的同一个方向的坐标值
# n行数据输入存放在列表中（图）
for i in range(n):
    s=str(input())
    graph.append([i for i in s])
# 表示输入的数据的图的状态
graph_state=[[0 for i in range(n)]for j in range(n)]


def dfs(x,y,cnt,p,q):  # x,y分别表示的是当前目标字母的横列坐标，cnt表示的是寻找的目标，p，q表示的是当前遍历的方向
    out[cnt]=[x,y]
    cnt+=1
    # 表示这一方向遍历的结果是题目要求的结果，把这一方向上的字母状态变成1
    if cnt==7:
        for a,b in out:
            graph_state[a][b]=1
    # 开始遍历八个大方向，    ##例如开始为向右边遍历
    elif p==0 and q==0:
        for k in range(8):
            x+=dx[k]
            y+=dy[k]
            if 0<=x<n and 0<=y<n and graph[x][y]==res[cnt]:  # 判断该坐标值是否符合要求
                dfs(x,y,cnt,dx[k],dy[k])    # 符合要求则进行递归操作继续进行该方向上的遍历操作
            # 回溯操作
            x-=dx[k]
            y-=dy[k]
    # 进行同一方向上的遍历操作
    else:
        x+=p
        y+=q
        if 0<=x<n and 0<=y<n and graph[x][y]==res[cnt]:  # 表示同一方向上的遍历操作的判断要是符合要求
            dfs(x,y,cnt,p,q)                             # 继续进行递归，对此方向继续遍历


# 寻找目标的第一个字母y
for i in range(n):
    for j in range(n):
        if graph[i][j]=="y":
            dfs(i,j,0,0,0)

# 输出矩阵，如果当前坐标字母的状态为1，则输出输入的数据，为0则输出  *
for i in range(n):
    for j in range(n):
        if graph_state[i][j]==0:
            print("*",end="")
        else:
            print(graph[i][j],end="")
    print()
