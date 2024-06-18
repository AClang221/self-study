"""
最大子段和
    题目描述
        给出一个长度为 n 的序列 a，选出其中连续且非空的一段使得这段和最大。
    输入格式
        第一行是一个整数，表示序列的长度 n。
        第二行有 n 个整数，第 i 个整数表示序列的第 i 个数字 a_i。
    输出格式
        输出一行一个整数表示答案。
    样例 #1
样例输入 #1

7
2 -4 3 -1 2 -4 3

样例输出 #1

4
"""
n=int(input())  # 表示序列长度
lst = [i for i in map(int,input().split())] # 将序列存入列表中
max_global=lst[0]   # 将第一个数定义为全局最大值
max_mub = lst[0]    # 将第一个数定义为当前最大值
# 从第二个数开始遍历
for i in range(1,len(lst)):
    max_mub=max(lst[i]+max_mub,lst[i]) # lst[i]表示当前遍历的数，lst[i]+max_mub表示的是当前子段和
    # 判断当前最大值是否大于全局最大值，是则替换全局最大值
    if max_mub>max_global:
        max_global=max_mub
print(max_global)
