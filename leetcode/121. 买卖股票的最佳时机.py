prices=[i for i in map(int,input().split())]
lst_re = sorted(prices,key=lambda x:x,reverse=True)
if lst_re==prices:
    print(0)
else:
    min_value=prices[0]
    max_value=0
    for i in range(1,len(prices)):
        max_value=max(prices[i]-min_value,max_value)
        min_value=min(min_value,prices[i])
    print(max_value)
