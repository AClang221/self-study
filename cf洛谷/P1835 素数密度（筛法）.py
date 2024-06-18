l, r = map(int, input().split())
N = int(r ** (1 / 2))
# 记录每个数的状态
is_prime = [True] * (N + 1)
# 素数表
prime = []
for x in range(2, N + 1):
    if is_prime[x]:  # 判断数据是否已经被划掉，没被划掉放入素数表中
        prime.append(x)
    i = 0
    while prime[i] * x <= N:  # 判断素数表中数据相乘，是否超过最大值
        # 循环不变式：pi一定是pi*x的最小质因数
        is_prime[prime[i] * x] = False
        if x % prime[i] == 0:  # 用于判断是否为最小质因数
            # 例如12，3*4=12，2*6=12如果不进行判断要被划两次，2是12的最小质因数，所以应该使用2*6来划去12
            break
        i += 1
# 创建字典进行哈希表打表
dis = {}
# 记录素数个数
ans = 0
# 将根号r范围内的素数进行求倍数操作，可以求出2-r之间的和数
for i in prime:
    if i < l:
        # 比如现在求2的倍数，但是l为101，那么101之前的2的倍数都可以忽略
        # 因此我们要取与l最接近的2的倍数，减少不必要的操作
        z = l - (l % i)
    else:
        z = i
    for j in range(z, r + 1, i):
        if j in dis:
            continue
        if l <= j != i:
            dis[j] = dis.get(i, i)
            ans += 1
if l == 1:
    print(r - l + 1 - ans - 1)
else:
    print(r - l + 1 - ans)
