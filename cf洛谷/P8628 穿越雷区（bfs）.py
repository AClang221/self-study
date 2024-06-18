# 表示有多少行数据
n=int(input())
# 将图进行存放
Map=[]
for i in range(n):
    s=[i for i in map(str,input().split())]
    # 寻找起始点
    if "A" in s:
        x,y=i,s.index("A")
    Map.append(s)
# 定义一下行走方向,dx表示纵向，dy表示横向，右下左上
f=[(0,1),(1,0),(0,-1),(-1,0)]
# 表示每一个点的状态，以及当前的值（走第几步）
Map_zt=[[-1 for i in range(n)]for j1 in range(n)]
Map_cs=[[0 for i in range(n)]for j2 in range(n)]
def bfs():
    # 将初始位置进行设置
    Map_zt[x][y]=0
    # 创建一个栈用于存放要走的点
    queue=[]
    # 将初始的位置添加到栈中
    queue.append((x,y))
    # 遍历知道全部点遍历结束
    while queue:
        x1,y1=queue.pop(0)
        for n_x,n_y in f:
            # 判断该移动是否会出界
            if pd(n_x+x1,n_y+y1):
                # 判断该点是否已经走过，并且所带能量是否相反
                if Map_zt[n_x+x1][n_y+y1]==-1 and Map[n_x+x1][n_y+y1]!=Map[x1][y1]:
                    # 将该位置设为已走
                    Map_zt[x1][y1] =0
                    # 纪录移动到该位置需要的步数
                    Map_cs[n_x+x1][n_y+y1]=Map_cs[x1][y1]+1
                    if Map[n_x+x1][n_y+y1]=="B":
                         return Map_cs[n_x+x1][n_y+y1]
                    else:
                        queue.append((n_x+x1,n_y+y1))
    return -1


def pd(x,y):
    return 0<=x<n and 0<=y<n


# 输出结果
print(bfs())