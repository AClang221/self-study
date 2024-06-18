# 导入库,双端队列
from collections import deque
N=int(input())

# 将数据点存储在列表中
Map=[input() for _ in range(N)]

# 寻找地图中的两个人P
P=[]
for i in range(N):
    for j in range(N):
        if Map[i][j]=="P":
            P.append(i)
            P.append(j)
# 创建四个移动方向，因为方向不可变性，元组的速度会比列表快
f=((1,0),(-1,0),(0,1),(0,-1))

# 创建四维列表，同时存放两个P的状态
Map_zt=[[[[-1]*N for _ in range(N)]for _ in range(N)]for _ in range(N)]

# 创建一个栈进行bfs操作
def bfs(P):
    queue=deque([P])
    Map_zt[P[0]][P[1]][P[2]][P[3]]=0

    while queue:
        # 原本的位置
        h1,l1,h2,l2=queue.popleft()
        for fx,fy in f:
            # 遍历方向后的位置
            hh1,ll1,hh2,ll2=h1+fx,l1+fy,h2+fx,l2+fy
            # 要是P1移动时撞到边界，或者碰到障碍物哪么位置不变
            if hh1<0 or ll1<0 or hh1>=N or ll1>=N or Map[hh1][ll1]=="#":
                hh1,ll1=h1,l1
            # 要是P2移动时撞到边界，或者碰到障碍物哪么位置不变
            if hh2<0 or ll2<0 or hh2>=N or ll2>=N or Map[hh2][ll2]=="#":
                hh2,ll2=h2,l2
            # 要是P1或者P2有一个在移动过程中没有受到阻碍，并且移动的位置之前没有到过，那么将移动次数赋值
            if (h1,l1,h2,l2) != (hh1,ll1,hh2,ll2) and Map_zt[hh1][ll1][hh2][ll2]==-1:
                Map_zt[hh1][ll1][hh2][ll2] =Map_zt[h1][l1][h2][l2]+1
                # 判断移动后两个点是否到达同一位置
                if hh1==hh2 and ll1==ll2:
                    return (Map_zt[hh1][ll1][hh2][ll2])
                else:
                    queue.append((hh1,ll1,hh2,ll2))
    return -1
# 将P作为一个元组导入
print(bfs(tuple(P)))