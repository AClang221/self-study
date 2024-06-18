"""
题目思路：
        将列表从小到大排序，利用二分库以及双指针的概念进行操作
        1.因为要求A-B的差C出现的次数，那么我们可以取列表最大值max减去C反向求有几个B
        2.B的值在列表中搜索如果存在则讲列表范围缩小，变为index0——index当前B的位置，并且B以及被取过不再进行二次存取所以取到B前一位
        3.如果列表max的前一位等于max，那么不进行求值直接把max的求出的B的个数加上即可
"""
import bisect                                                               # 引用二分库
N, C = map(int, input().split())                                            # N， C 分别表示列表中元素的个数和要求的差的值
lst = list(map(int, input().split()))
d_x = sorted(lst, key=lambda x: x, reverse=False)

ans = 0                                                                     # ans表示返回的值
left = 0                                                                    # left定义左边界
right = len(d_x)-1                                                          # 定义右边界
goal_last = d_x[right] - C                                                  # 用来存放要求的上一个B的
goal = d_x[right] - C                                                       # 用来存放当前要求的B的值
hi_right = len(d_x)-1                                                       # 二分查找范围的右边界
while left < right:                                                         # 对撞指针的概念碰到一起时指针停止运行
    ans_new = 0                                                             # 这个用来存放当前A—C可以找到的B的数量
    """进行查找符合条件的B的个数"""
    while d_x[bisect.bisect_right(d_x, goal, left, hi_right)-1] == goal:    # 因为bisect_right求出的是查找目标元素的右边的位置，减去1要是和查找目标相等说明目标存在
        ans_new += 1                                                        # 目标存在当前A—C可以找到的B的数量加上1
        hi_right = bisect.bisect_right(d_x, goal, left, hi_right)-1         # 右边界内收，继续向左边查找
    else:
        right -= 1                                                          # 没有目标值将max的下标变小往左寻找较小的最大值
    ans += ans_new                                                          # 总记加上当前的小计
    goal = d_x[right] - C                                                   # 取当前A—C的值B
    """用来判断下一个要取的B是否与当前一样"""
    while goal == goal_last:                                                # 当前要求的B与上一个相等说明可以找到的B的个数是一样的
        right -= 1                                                          # 将max的下表继续往左移
        ans += ans_new                                                      # 所以直接加上B的个数
        goal = d_x[right] - C

    goal_last = goal
print(ans)
