total={}
for i in list((map(str,input().split(",")))):
    i=str.strip(i)
    total[i]=total.get(i,0)+1   # get(key,value)    如果key的值不存在则返回value的值，value可以不写
up=sorted(total.items(),key=lambda x:x[1],reverse=True)
for i in range(len(up)-1):
    print("%s:%d"%(up[i][0],up[i][1]))
print("%s:%d"%(up[len(up)-1][0],up[len(up)-1][1]),end='')
