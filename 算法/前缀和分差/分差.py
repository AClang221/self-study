"""
输入一个长度为 n的整数序列。
接下来输入 m个操作，
每个操作包含三个整数 l,r,c，表示将序列中 [l,r]之间的每个数加上 c
请你输出进行完所有操作后的序列。

第一行包含两个整数 n和 m
第二行包含 n个整数，表示整数序列。
接下来 m行，每行包含三个整数 l，r，c表示一个操作。

输入样例：
6 3
1 2 2 1 2 1
1 3 1
3 5 1
1 6 1
输出样例：
3 4 5 3 4 2
"""
n, m = map(int, input().split())
a_lst = list(map(int, input().split()))      # 输入的原成绩
b_lst = [0]*(n+1)                           # 构造一个原成绩的差分列表
b_lst[0] = a_lst[0]                         # 使得a_lst[n]=b1+b2+b3+b4+----bn
for i in range(1, n):
    b_lst[i] = a_lst[i]-a_lst[i-1]
while m > 0:
    l, r, c = map(int, input().split())
    b_lst[l-1] += c
    b_lst[r] -= c
    m -= 1
res = [0]*(n+1)                               # 新建一个列表用来求b的前缀和
for i in range(1, n+1):
    res[i] = res[i-1] + b_lst[i-1]
for i in res[1:]:
    print(i, end=" ")


"""
思路：
    此处将列表第一个下表当作1
    bl+c
    al = b1+b2+b3+b4+----+bl+c
    a(l+1) = b1+b2+b3+b4+----+bl+c+b(l+1)
    以此类推
    b（r+1）-c
    ar = b1+b2+b3+b4+--+bl+c--+br
    a(r+1) = b1+b2+b3+b4+--+bl+c--+br+b(r+1)-c
    a(r+1) = b1+b2+b3+b4+--+bl+c--+br+b(r+1)-c+b(r+1)
    以此类推
通过以上求前缀和可以将al---ar都加上一个c
"""
# 差分算法：可以通过修改两个边界值来对区间上的值进行同加减的修改