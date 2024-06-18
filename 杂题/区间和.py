"""
给定n个正整数组成的数列
输入格式
第一行，为一个正整数n
第二行，为n个正整数
第三行，为一个正整数 m
接下来 m 行，每行为两个正整数l,r
输出格式
共m行。
第 i行为第 i 组答案的询问。
样例
样例输入 #1

```
4
4 3 2 1
2
1 4
2 3
```

### 样例输出 #1

```
10
5
```
"""
"""
# 暴力（太慢了）
n = int(input())
lst = list(map(int, input().split()))
m = int(input())
for i in range(m):
    x, y=map(int, input().split())
    total = 0
    for j in range(x-1, y):
        total += lst[j]
    print(total)
"""
# 前缀和差
n = int(input())
lst = list(map(int,input().split()))
lst_total = [0]
total =0
for i in lst:
    total += i
    lst_total.append(total)
m = int(input())
for i in range(m):
    l, r = map(int,input().split())
    print(lst_total[r]-lst_total[l-1])
