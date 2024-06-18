n = int(input())
graph = [[0 for i in range(n+1)]for j in range(n+1)]   # 创建一个图,必须要从1开始不然会错
total = 0                                          # 表示符合要求的次数


def check(x,y):
    for i in range(1,x):      # 判断上一行列上有没有棋子
        if graph[i][y]:
            return False

    for i in range(1,min(x,y)):       # 判断上一行左上方有没有棋子
        if graph[x-i][y-i]:
            return False

    for i in range(1,min(x,n-y)+1):       # 判断上一行右上方有没有棋子
        if graph[x-i][y+i]:
            return False

    return True

# 打印输出
def print_out():
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j]:
                print(j,end=" ")
    print()


def dfs(x):
    global total
    # 判断整行是否遍历结束
    if x>n:
        total+=1
        # 判断是不是前三个解，是的话打印输出
        if total<=3:
            print_out()
        return

    for i in range(1,n+1):
        # 判断合法性
        if check(x,i):
            graph[x][i]=1
            # 进入下一行
            dfs(x+1)
            graph[x][i]=0

dfs(1)
print(total)