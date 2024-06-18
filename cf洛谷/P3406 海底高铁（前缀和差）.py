# 定义N,M分别表示铁路经过的城市数量和要去的城市数量
N,M=map(int,input().split())
# 顺序记录要去的地方
path=[i for i in map(int,input().split())]
# 记录到每个城市的票价以及办卡的费用
ticket=[]
for i in range(N-1):
    a,b,c=map(int,input().split())
    ticket.append((a,b,c))
# 建一个前缀差表
time_fc=[0]*(N+1)
# 前缀和差进行计算每个城市经过的次数
# 前缀差操作
for i in range(M-1):
    time_fc[max(path[i],path[i+1])]-=1
    time_fc[min(path[i],path[i+1])]+=1
# 建立前缀和表格
time=[]
# 前缀和操作
time.append(time_fc[1])
for i in range(2,N):
    time.append(time[i-2]+time_fc[i])
# 表示一共要多少钱
total=0
# 判断买票还是办卡
for i in range(N-1):
    if ticket[i][0]*time[i]<=ticket[i][1]*time[i]+ticket[i][2]:
        total+=ticket[i][0]*time[i]
    else:
        total+=ticket[i][1]*time[i]+ticket[i][2]
print(total)