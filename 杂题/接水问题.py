"""---------------------生成二维数组-----------------------------"""
height = list(map(int, input().split()))
height_max = max(height)
lst = [[0]*len(height) for i in range(0, height_max)]
"""------------------------将数据放入到二维数组中----------------------"""
for i in range(0 ,len(height)):
    if height[i] != 0:
        for j in range(0, height[i]):
            lst[j][i] = 1
"""------------------判断有多少格水------------"""
water = 0
for i in range(height_max):
    start = 0
    count = 0
    for j in range(len(height)):
        if lst[i][j] == 1:
            start =1
            water += count
            count = 0
        if start == 1 and lst[i][j] != 1:
            count += 1
"""--------------------打印结果--------------"""
print(water)
