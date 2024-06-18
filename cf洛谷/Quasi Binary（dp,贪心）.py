# 将数字拆分后反方向排序
n = list(reversed(input()))
# 因为每一位数最大的值为9，所以只需要建立长度为9的列表即可
outs = [0] * 9
for i in range(len(n)):
    for x in range(int(n[i])):
        outs[x] += 10 ** i
# 将列表中值为0的全部移除然后生成一个新的列表
outs = list(filter(None, outs))
print(len(outs))
# *操作符在这里用于展开列表，使得列表中的每个元素都作为单独的参数传递给print函数
print(*outs)