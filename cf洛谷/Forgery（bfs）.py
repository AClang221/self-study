# 表示输入数据有n行m列
n,m=map(int,input().split())
# 用于存方数据
Map=[]
for i in range(n):
    Map.append(list(input()))
# 复制一份数据
Map_cp=[]
for i in Map:
    # copy
    Map_cp.append(i.copy())

def pin(x,y):
    Map_cp[x - 1][y] = '.'
    Map_cp[x + 1][y] = '.'
    Map_cp[x][y - 1] = '.'
    Map_cp[x][y + 1] = '.'
    Map_cp[x - 1][y - 1] = '.'
    Map_cp[x - 1][y + 1] = '.'
    Map_cp[x + 1][y - 1] = '.'
    Map_cp[x + 1][y + 1] = '.'


def pd(x,y):
    if Map[x - 1][y] == '.':
        return False
    if Map[x + 1][y] == '.':
        return False
    if Map[x][y - 1] == '.':
        return False
    if Map[x][y + 1] == '.':
        return False
    if Map[x - 1][y - 1] == '.':
        return False
    if Map[x - 1][y + 1] == '.':
        return False
    if Map[x + 1][y - 1] == '.':
        return False
    if Map[x + 1][y + 1] == '.':
        return False
    return True

for i in range(1,n-1):
    for j in range(1,m-1):
        # 判断当前位置是否符合条件将周围的方向进行修改
        if pd(i,j):
            # 符合的话将这几个位置进行修改
            pin(i,j)
t=1
# 判断修改过后的数据，要是里面有  ”.“ 说明经过修改的数据无法达到题目所要求的模样
# 因为一开始的数据全是”.“
for i in Map_cp:
    t="".join(i)
    if "#" in t:
        print("NO")
        t=0
        break
if t:
    print("YES")