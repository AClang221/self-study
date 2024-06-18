n = int(input())
lst = [i for i in map(int, input().split())]
# 分别表示，休息天数，此刻状态，遍历
ans = 0
zt = 3
time = 0
while time < n:
    # 判断要是zt=3，说明现在可以进行比赛也可以健身，为1说明现在不能进行1的操作
    if lst[time] == 0:
        ans += 1
        zt = 3
    elif lst[time] == 1:
        if zt != 1:
            zt = 1
        else:
            ans += 1
            zt = 3
    elif lst[time] == 2:
        if zt != 2:
            zt = 2
        else:
            ans += 1
            zt=3
    elif lst[time] == 3:
        if zt == 1:
            zt = 2
        elif zt == 2:
            zt = 1
    time += 1
# 要是连续出现3，直接忽略不管
print(ans)