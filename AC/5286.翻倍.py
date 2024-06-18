"""
因为a，b分别进行翻倍相乘相当于a,b相乘翻三倍
将ab相乘开三次，如果可以开出整数说明有可能实现分别翻倍到a,b
但是有例外比如8，27相乘开三次得6，但是没法翻倍到8，27
所以要进行判定，将开出来的数分别除以a,b
如果余数为0则为yes
7，8，9，10行因为开三次方计算机计算的结果和实际结果有出入，所以要进行此次操作
https://www.bilibili.com/video/BV1je411X7md/?spm_id_from=333.1007.top_right_bar_window_history.content.click
b站y总视频讲解
"""
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    total = a * b
    ans = int(total ** (1/3))
    if (ans+1) ** 3 == total:
        ans += 1
    elif (ans-1) ** (1/3) == total:
        ans -= 1
    if a % ans != 0 or b % ans != 0:
        print("No")
    elif ans ** 3 != total:
        print("No")
    else:
        print("Yes")
