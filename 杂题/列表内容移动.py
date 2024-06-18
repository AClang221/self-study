"""
给定两个字符串，A和B。
A的旋转操作就是将A最左边的字符移动到最右边。
例如，若A='abcde，在移动一次之后结果就是'bcdea'。
如果在若干次调整操作之后，A能变成B，那么返回True。
如果不能匹配成功，则返回false
"""
A = list(input())
B = list(input())
val = 0
for i in range(len(A)-1):
    if A == B:
        val = 1
        break
    else:
        A.append(A[0])
        A.remove(A[0])
if val == 0:
    print("NONE")
else:
    print("TRUE")
