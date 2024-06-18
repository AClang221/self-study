"""
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :

输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :

输入: 9973
输出: 9973
解释: 不需要交换。
"""

# 输入数据
num=int(input())
# 将数据放入列表中
digits = [int(d) for d in str(num)]
# 生成一个字典存放每个数字出现的最后位置
indices = {x: i for i, x in enumerate(digits)}
# 遍历列表中的每个数字
for i,x in enumerate(digits):
    # 判断在这个数字的右边是否存在比他大的数（从9开始）
    for d in range(9,x,-1):
        # 如果存在，则交换两个数字的位置
        if indices.get(d,-1)>i:
            digits[i],digits[indices[d]]=digits[indices[d]],digits[i]
            break
# 输出结果
print(int("".join(map(str,digits))))