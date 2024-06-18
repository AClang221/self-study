def left(pos,water):
    if pos+1==n:
        return True
    if pos+k>=n:
        return True
    if pos>water and l_wall[pos+1]=="-" and zt_l[pos+1]:
        queue.append((pos + 1, 0,water+1))
        zt_l[pos+1]=0
    if pos-2>water and l_wall[pos-1]=="-" and zt_l[pos - 1]:
        queue.append((pos-1,0,water+1))
        zt_l[pos - 1] = 0
    if pos>water and r_wall[pos+k]=="-" and zt_r[pos + k]:
        queue.append((pos+k,1,water+1))
        zt_r[pos + k] = 0
    return False


def right(pos,water):
    if pos+1==n:
        return True
    if pos+k>=n:
        return True
    if pos>water and r_wall[pos+1]=="-" and zt_r[pos+1]:
        queue.append((pos + 1, 1,water+1))
        zt_r[pos + 1]=0
    if pos-2>water and r_wall[pos-1]=="-" and zt_r[pos - 1]:
        queue.append((pos-1,1,water+1))
        zt_r[pos - 1]=0
    if pos>water and l_wall[pos+k]=="-" and zt_l[pos + k]:
        queue.append((pos+k,0,water+1))
        zt_l[pos + k]=0
    return False

n,k=map(int,input().split())
l_wall=[i for i in list(str(input()))]
r_wall=[i for i in list(str(input()))]
zt_l=[1 for _ in range(n)]
zt_r=[1 for _ in range(n)]
queue=[(0,0,-1)]


def dfs():
    while queue:
        # 分别表示位置,方向,水的高度
        pos,dir,water=queue.pop()
        if dir==0:
            if left(pos,water):
                return "YES"
        else:
            if right(pos,water):
                return "YES"

    return "NO"


print(dfs())