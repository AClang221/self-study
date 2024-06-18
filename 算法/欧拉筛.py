def find_prime(n):
    prime = []  # 生成一个素数表
    for x in range(2, n+1):
        if is_prime[x]:  # 判断数据是否已经被划掉，没被划掉放入素数表中
            prime.append(x)
        i = 0
        while prime[i] * x <= n:  # 判断素数表中数据相乘，是否超过最大值
            # 循环不变式：pi一定是pi*x的最小质因数
            is_prime[prime[i] * x] = False
            if x % prime[i] == 0:  # 用于判断是否为最小质因数
                # 例如12，3*4=12，2*6=12如果不进行判断要被划两次，2是12的最小质因数，所以应该使用2*6来划去12
                break
            i += 1
    return prime


n = int(input())
is_prime = [True] * (n+1)  # 生成一个列表对应每一个数字，Ture表示没被划掉
print(find_prime(n))
