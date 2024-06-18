a, b = 0, 1
n = int(input())
t = 1
while t <= n:
    print(a,end = " ")
    c = a + b
    a,b = b,c
    t += 1 