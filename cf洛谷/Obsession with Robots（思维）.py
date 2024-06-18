"""
本题的主要思路就是
遍历方向并进行判断
                1.要是走重复路线必定不是最优解
                2.要是下一步要走的路线，例外三个方向上有任何一个点已经走过，那必然也不是最短路线
"""
s=str(input())
MAP=[[0 for i in range(210)]for j in range(210)]
# x表示行，y表示列，设定一个初始位置
x,y=105,105
# 将初始位置设为已经走过
MAP[105][105]=1
zt=0
# 进行遍历
for i in s:
    if i=="L":
        if MAP[x][y-1]==0 and MAP[x][y-2]==0 and MAP[x+1][y-1]==0 and MAP[x-1][y-1]==0:
            y-=1
            MAP[x][y]=1
        else:
            zt=1
            break
    elif i=="R":
        if MAP[x][y+1]==0 and MAP[x][y+2]==0 and MAP[x+1][y+1]==0 and MAP[x-1][y+1]==0:
            y+=1
            MAP[x][y] = 1
        else:
            zt=1
            break
    elif i=="U":
        if MAP[x-1][y]==0 and MAP[x-2][y]==0 and MAP[x-1][y-1]==0 and MAP[x-1][y+1]==0:
            x-=1
            MAP[x][y] = 1
        else:
            zt=1
            break
    elif i=="D":
        if MAP[x+1][y]==0 and MAP[x+2][y]==0 and MAP[x+1][y-1]==0 and MAP[x+1][y+1]==0:
            x+=1
            MAP[x][y] = 1
        else:
            zt=1
            break
# 程序输出
if zt==1:
    print("BUG")
else:
    print("OK")