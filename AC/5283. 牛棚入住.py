n, a, b = map(int, input().split())
little = [0] * a
big = [[0 for i in range(2)] for x in range(b)]
big_sheng = []
ans = 0


def one():
    global ans
    if len(little) != 0:
        little.pop()
    elif len(little) == 0 and len(big) != 0:
        big.pop()
        big_sheng.append(0)
    elif len(little) == 0 and len(big) == 0 and len(big_sheng) != 0:
        big_sheng.pop()
    else:
        ans += 1


def two():
    global ans
    if len(big) != 0:
        big.pop()
    else:
        ans += 2

lst = list(map(int, input().split()))

for i in lst:
    if i == 1:
        one()
    else:
        two()
print(ans)
