n=int(input())
lstw = []
lsth = []
lsthb = []
maxh = 0
sumw = 0
maxh2 = 0
for i in range(n):
    w, h = map(int, input().split())
    lstw.append(w)
    lsth.append(h)
lsthb = lsth[0:n]
lsthb.sort(reverse=True)
if lsthb[0] == lsthb[1]:
    maxhg = 2
    maxh = max(lsth)
else:
    maxhg = 1
    maxh = max(lsth)
    lsthb.remove(max(lsthb))
    maxh2 = max(lsthb)
for i in range(n):
    sumw += lstw[i]
if maxhg == 1:
    for i in range(n):
        if lsth[i] == maxh:
            sumw -= lstw[i]
            print(maxh2*sumw, end=" ")
            sumw += lstw[i]
        else:
            sumw -= lstw[i]
            print(maxh*sumw, end=" ")
            sumw+=lstw[i]
else:
    for i in range(n):
        sumw -= lstw[i]
        print(maxh*sumw, end=" ")
        sumw += lstw[i]
