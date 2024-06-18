def fun():
    size = int(input())
    # 定义一个偶数
    even=0
    # 定义一个奇数
    odd=0
    # 定义第一个全局最小
    total=1e9
    for i in input().split():
        mub=int(i)
        # 判断是否为奇数
        if mub & 1:
            odd+=1
        else:
            even+=1
            t=0
            # 为偶数的话进行以为操作知道变为奇数位置，并记录操作次数
            while not(mub & 1):
                t+=1
                mub>>=1
            # 实时记录最少操作次数
            total=min(total,t)
    # 如果偶数不为0
    if even:
        # 判断奇数个数
        if odd:
            # 奇数不为0，打印偶数
            print(even)
        else:
            # 否则打印偶数个数加上操作次数减去1
            print(total+even-1)
    # 如果偶数为0
    else:
        print(0)






if __name__=="__main__":
    for n in range(int(input())):
        fun()