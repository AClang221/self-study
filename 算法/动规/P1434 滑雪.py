"""
滑雪
题目描述
    滑雪为了获得速度，滑的区域必须向下倾斜，而且当你滑到坡底，你不得不再次走动，想知道在一个区域中最长的滑坡。
    区域由一个二维数组给出。数组的每个数字代表点的高度。下面是一个例子：
    plain
    1   2   3   4   5
    16  17  18  19  6
    15  24  25  20  7
    14  23  22  21  8
    13  12  11  10  9
    一个人可以从某个点滑向上下左右相邻四个点之一，当且仅当高度会减小。
    在上面的例子中，一条可行的滑坡为 24-17-16-1（从 24 开始，在 1 结束）
    当然    25－24－23－。。。。。－3－2－1 更长。事实上，这是最长的一条。
输入格式
    输入的第一行为表示区域的二维数组的行数 $R$ 和列数 $C$。下面是 $R$ 行，每行有 $C$ 个数，代表高度(两个数字之间用 $1$ 个空格间隔)。
输出格式
    输出区域中最长滑坡的长度。
样例 #1
### 样例输入 #1
```
5 5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
```
样例输出 #1
```
25
```
"""

def dfs(x, y):
    # 判断是否遍历过当前位置
    if Map_max[x][y] != 0:
        return Map_max[x][y]
    f = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 生成四个方向
    # 开始遍历四个方向
    for fx, fy in f:
        nx, ny = fx + x, fy + y
        if 0 <= nx < R and 0 <= ny < C and Map[nx][ny] < Map[x][y]:  # 判断是否符合条件
            Map_max[x][y] = max(Map_max[x][y], dfs(nx, ny))          # 实时更新x，y点上的最大值
    Map_max[x][y] += 1
    return Map_max[x][y]


def dp():
    # 定义一个全局最大值
    global_max=0
    # 开始进行每个位置的遍历
    for i in range(R):
        for j in range(C):
            # 实时更新最大值
            global_max=max(global_max,dfs(i,j))
    return global_max


R,C=map(int,input().split())    # 输入R,C表示图的大小
Map = [[i for i in map(int,input().split())]for _ in range(R)]  # 构建一个二维列表存放输入的数据
Map_max=[[ 0 for _ in range(C)]for _ in range(R)]               # 构建一个二位列表存放当前位置能构建的最长路线
# 开始进行动态规划求解
print(dp())