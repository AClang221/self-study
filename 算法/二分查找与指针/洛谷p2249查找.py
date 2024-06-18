"""
思路：
    二分查找与指针
    判断  bisect.bisect_left 与 bisect.bisect_right  两者相等说明列表中没有要查找的值
    要是不相等说明有，返回bisect.bisect_left+1的值因为不加1返回的是第一次出现左边的值
"""
import bisect
n, m=map(int, input().split())
lst = list(map(int, input().split()))
lst_cha = list(map(int, input().split()))
for i in lst_cha:
    z = bisect.bisect_left(lst, i)
    y = bisect.bisect_right(lst, i)
    if z == y:
        print(-1, end=" ")
    else:
        print(bisect.bisect_left(lst, i)+1, end=" ")
