"""
在n×n 的格子上有m个地毯。
给出这些地毯的信息，问每个点被多少个地毯覆盖。
第一行，两个正整数 n,m。意义如题所述
接下来m行，每行两个坐标（x1,y1）和（x2,y2）,代表一块地毯，左上角是（x1,y1），右下角（x2,y2）
"""
n, m = map(int, input().split())
carpet_lst = [[0 for i in range(n+1)]for j in range(n)]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1-1,x2):
        carpet_lst[x][y1-1] += 1
        carpet_lst[x][y2] -= 1
ans_lst = [[0 for i in range(n+1)]for j in range(n)]
for i in range(n):
    for j in range(1,n+1):
        ans_lst[i][j] = ans_lst[i][j-1] + carpet_lst[i][j-1]
for x in range(n):
    for y in range(1,n+1):
        print(ans_lst[x][y],end=" ")
    print()
