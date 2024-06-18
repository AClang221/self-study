def bag():
    value = [[0 for i in range(T+1)]for j in range(M+1)]
    for i in range(1,M+1):
        for j in range(1,T+1):
            value[i][j]=value[i-1][j]
            if j>=data[i-1][0] and value[i][j]<value[i-1][j-data[i-1][0]]+data[i-1][1]:
                value[i][j]=value[i-1][j-data[i-1][0]]+data[i-1][1]
    return value[M][T]


T,M=map(int,input().split())
data = [[i for i in map(int,input().split())]for j in range(M)]
print(bag())