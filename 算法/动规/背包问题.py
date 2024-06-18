def bag(count, Totalweight, weight, cost):
    value = [[0 for i in range(Totalweight+1)]for j in range(count+1)]    # 创建一个初始化背包
    for i in range(1,count+1):          # 遍历背包中的每一件物品，从第1件开始
        for j in range(1,Totalweight+1):    # 遍历背包的容量，从重量为1开始
            value[i][j] = value[i-1][j]       # 将当前背包价值设置为上一个物品的同重量下的价格

            # 进行判断，如果当前背包容量大于等于物品的重量，并且上一物品价值小于当前物品价值加剩余空间价值，则改变其价值
            if j >= weight[i-1] and value[i][j] < value[i-1][j-weight[i-1]]+cost[i-1]:
                # 因为value[i][j]=value[i-1][j]所以其为上一物品价值
                # cost[i-1]为当前物品价值
                # value[i-1][j-weight[i-1]]为剩余空间价值

                value[i][j] = value[i-1][j-weight[i-1]]+cost[i-1]
    return value


def show(count,Totalweight,weight,value):
    x=[False for i in range(count)]         # 表示每件物品的当前状态
    j = Totalweight                         # 因为背包中的最大值一定在背包的最后一列
    for i in range(count,0,-1):             # 从背包的底部开始遍历，因为最右下的值永远是最大的
        # 开始遍历
        if value[i][j] > value[i-1][j]:
            x[i-1] = True
            j -= weight[i-1]
    print("最大价值为：",value[count][Totalweight])   # 输出最大值
    for i in range(count):
        if x[i]:
            print("第",i+1,"个",end="   ")


count = int(input())        # 表示物品的数量
Totalweight = int(input())  # 表示背包可以承受的最大重量
weight = [i for i in map(int,input().split())]    # 表示每件物品的重量
cost = [i for i in map(int,input().split())]   # 表示每件物品的价值
value = bag(count,Totalweight,weight,cost)       # 调用背包函数开始进行dp
show(count,Totalweight,weight,value)           # 调用show函数进行结果的输出
