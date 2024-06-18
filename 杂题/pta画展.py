"""
本次画展共展示了来自5个城市若干个作品，为了区分不同的城市的作品，负责人用五种不同的标签代表五个城市。
并将其制作成一个平面图放在画廊门口供人们参考，
以下为代表五种城市的标签（标签大小为一个4×4的字符矩阵构成）：

一号城市：

....
....
....
....
二号城市：

****
....
....
....
三号城市：

****
****
....
....
四号城市：

****
****
****
....
五号城市：

****
****
****
****
负责人将所有标签摆放成一个n行，m列的平面图，不同的标签之间用#表示。

现在给出平面图，请你求出1∼5号城市的作品分别有几个。

输入格式:
输入的第一行给出两个整数n,m——表示标签摆放共有n行m列。

接下来给出5×n+1行，每行5×m+1个字符，表示描述每一幅画属于城市的标签。边缘用#分割。

题目保证内部只有可能是题目给出的五种状态。

1≤n,m≤100

输出格式:
一行中输出5个整数——依次表示1∼5号城市的作品的数量。

输入样例:
2 3
################
#****#****#****#
#****#****#****#
#****#....#****#
#....#....#****#
################
#....#****#****#
#....#****#....#
#....#....#....#
#....#....#....#
################
输出样例:
1 1 2 1 1
"""
n, m = map(int, input().split())
ans = [0, 0, 0, 0, 0]  # 表示每个城市的作品数量


def get():
    anr = [0]*m
    z = input()  # 将第一行#边框消耗掉
    for i in range(4):  # 因为每一幅画有四行
        t = input()  # 将画的每一行进行判断
        for j in range(m):  # 如果为*则加一，因为由题可知，*代表城市等级
            if t[j*5+1] == "*":
                anr[j] += 1  # 例如四行都为*则anr=4，然后进行下列for循环
    for x in anr:
        ans[x] += 1  # 因为anr为四所以ans[anr=4的时候]表示的是ans中第五个数，即第五城市


for i in range(n):  # 将以上函数中的内容进行的次数
    get()
h = input()  # 将结尾的#消耗掉
"""结尾将结果进行输出"""
for i in range(4):
    print(ans[i], end=" ")
print(ans[4])
