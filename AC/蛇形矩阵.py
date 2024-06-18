y, x = map(int, input().split())
lst = [[0]*x for i in range(y)]
left = 0; right = x;top = 0; down = y
start = 1
while 1:
    for i in range(left, right):
        lst[left][i] = start
        start += 1
    top += 1
    if top > down-1:
        break
    for i in range(top, down):
        lst[i][right-1] = start
        start += 1
    right -= 1
    if left> right-1:
        break
    for i in range(right-1, left-1, -1):
        lst[down-1][i] = start
        start += 1
    down -= 1
    if top> down-1:
        break
    for i in range(down-1, top-1, -1):
        lst[i][left] = start
        start += 1
    left += 1
    if left > right-1:
        break
for i in range(len(lst)):
    for j in range(len(lst[0])):
        print(lst[i][j], end=" ")
    print()
