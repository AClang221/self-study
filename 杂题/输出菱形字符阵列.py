lst = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
mub = int(input())
a=0
for i in range(mub):
    print(" " * (mub-i-1),end="")
    print(lst[i]*(i*2+1))
for i in range(mub-1,0,-1):
    a+=1
    print(" " * a,end="")
    print(lst[i-1]*(i*2-1))