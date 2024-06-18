"""
本题采用二分思路对时间进行二分查找操作

"""
def check(ans):
    # q表示ans时间内电池可以提供的电量
    q=p*ans
    # sum表示设备电量不够需要补充电的量
    sum=0
    for i in range(n):
        # 要是在ans时间内该设备需要的电量小于自身所带电量则不需要电池供电
        if ai[i]*ans<=bi[i]:
            continue
        else:
            # 反之需要的电量减去原有的电量，就是需要电池供电的电量
            sum+=(ai[i]*ans-bi[i])
    # 判断可以提供的电与需要提供的电的大小
    return sum<=q


# n表示设备数量，p表示一秒钟可以充电的量
n,p=map(int,input().split())
# 创建数组a,b分别存储每台设备的每秒用电以及初始电量
ai=[0]*(n+1)
bi=[0]*(n+1)
for i in range(n):
    ai[i],bi[i]=map(int,input().split())
# 特判当需要的电量小于等于能提供的电量时，设备可以无限使用
if sum(ai)<=p:
    print(-1)
else:
    # 二分查找，设置左右边界
    l,r=float(0),float(1e10)
    # 表示精确度
    while r-l>1e-6:
        # mid表示最多可以使用的时间，二分查找先取中间值
        mid=float((l+r)/2)
        # 进行判断，要是在mid时间内，没有设备电量掉到0，那么说明可以坚持的时间在mid到r的范围中
        # 所以将二分左边范围移动到mid处，即l=mid
        # 反之则r=mid
        if check(mid):
            l=mid
        else:
            r=mid
    # 输出答案
    print("%.10f"%mid)
