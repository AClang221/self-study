# 定义N,M分别表示铁路经过的城市数量和要去的城市数量
N,M=map(int,input().split())
# 定义path列表来存储路线
path=[i for i in map(int,input().split())]
# 定义ticket列表用来存储票价
ticket=[]
for i in range(N-1):
    a,b,c=map(int,input().split())
    ticket.append((a,b,c))
# 创建差分列表
time_fc=[0]*(N+1)
for i in range(M-1):
    # 利用差分特性，左边界加一，右边界减一，来实现数据的同加减，此处用于求这段路重复走过多少次
    time_fc[max(path[i],path[i+1])]-=1
    time_fc[min(path[i],path[i+1])]+=1
# 创建浅醉和列表，用于求每块路线走过的次数
time=[]
# 进行前缀和操作
time.append(time_fc[1])
for i in range(2,N):
    time.append(time[i-2]+time_fc[i])
# 统计一共花费
total=0
for i in range(N-1):
    if ticket[i][0]*time[i]<=ticket[i][1]*time[i]+ticket[i][2]:
        total+=ticket[i][0]*time[i]
    else:
        total+=ticket[i][1]*time[i]+ticket[i][2]
print(total)