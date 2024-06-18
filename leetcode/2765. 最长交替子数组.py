nums=[i for i in map(int,input().split())]
lst = [0] * (len(nums) + 1)
lst[0] = 1
for i in range(1, len(nums)):
    lst[i] = nums[i] - nums[i - 1]
max_len = 1
chang = 1
ans = 1
for i in range(1, len(lst)):
    if lst[i] == 1 and ans == 1:
        chang += 1
        ans = -1
    elif lst[i] == -1 and ans == -1:
        chang += 1
        ans = 1
    elif lst[i] == 1 and ans == -1:
        max_len = max(chang, max_len)
        chang = 2

    else:
        max_len = max(chang, max_len)
        chang = 1
        ans = 1
if max_len==1:
    max_len=-1
print(max_len)