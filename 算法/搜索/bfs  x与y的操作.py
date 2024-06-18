"""
给你两个正整数x和y。
一次操作中，你可以执行以下四种操作之一:
1.如果x是11的倍数，将x除以11。
2.如果x是5的倍数，将x除以5
3.将x减1。
4.将x加1
请你返回让x和y相等的最少操作次数
"""
x,y=map(int,input().split())
f=[1,-1]
status=[]
def bfs(x):
    status.append(x)
    if x == y:
        return 0
    queue=[]
    queue.append((x,0))
    while queue:
        x,t=queue.pop(0)
        if x%11==0 and x>y:
            x1=x/11
            if x1==y:
                return t+1
            if x1 not in status:
                queue.append((x1,t+1))
                status.append(x1)
        if x%5==0 and x>y:
            x1=x/5
            if x1==y:
                return t+1
            if x1 not in status:
                queue.append((x1,t+1))
                status.append(x1)
        for i in f:
            x1=x+i
            if x1 == y:
                return t + 1
            if x1 not in status:
                status.append(x1)
                queue.append((x1,t+1))
print(bfs(x))