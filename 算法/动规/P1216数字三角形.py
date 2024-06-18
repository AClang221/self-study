def dp(n, tower):
    Map = [[0]*i for i in range(1, n+1)]    # 创建一个与输入数据一一对应的图，用来保存这个值的当前状态
    Map[0][0]=tower[0][0]   # 塔顶
    for i in range(1,n):    # 从金字塔的第二层开始遍历
        for j in range(i+1):    # 遍历金字塔里面的每一个数字
            # 要是遍历的是第一个数，它只能由上一层的第一个数走到
            if j==0:
                Map[i][j]=Map[i-1][j]+tower[i][j]
            # 要是当前遍历的数不是开头不是结尾他的状态会由上一行的第j个和j-1个的状态决定，因为题目要求找最大值，所以将大的值保留下来当作是当前位置的状态
            elif 0<j<i:
                Map[i][j]=max(Map[i-1][j]+tower[i][j],Map[i-1][j-1]+tower[i][j])
            # 要是遍历到了当前层数的最后一个数，它只能通过上一行最后一个值走到
            else:
                Map[i][j] = Map[i - 1][j-1] + tower[i][j]
    # 返回Map最后一行的最大值
    return max(Map[n-1])


# 输入金字塔的行数
n=int(input())
# 将每行的数据存入一个二位列表中
tower = [[i for i in map(int,input().split())]for j in range(n)]
# 调用函数进行求解并输出
print(dp(n,tower))