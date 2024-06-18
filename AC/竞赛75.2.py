
"""
ls = [[1,2],[3,6],[2,5]]
ls = sorted(ls,key=lambda x:x[1])
"""

frequency = int(input())
identity_lst = ["rat","woman", "man", "captain"]
name_identity =[]
for i in range(frequency):
    name_identity.append(input().split())
    name_identity[i].append(i)
    if name_identity[i][1] in identity_lst:
        name_identity[i].append(identity_lst.index(name_identity[i][1]))
    else:
        name_identity[i].append(1)
name_identity =sorted(name_identity ,key= lambda x:x[3])
start = 0
down = 0
for i in range(frequency):
    if name_identity[i][3]==1:
        start = name_identity.index(name_identity[i])
        break
for i in range(frequency-1,-1,-1):
    if name_identity[i][3] == 1:
        down = name_identity.index(name_identity[i])
        break
center = name_identity[start:down+1]
center=sorted(center ,key= lambda x:x[3])
left = name_identity[0:start+1]
right = name_identity[down:frequency+1]
name_identity = []
name_identity.extend(left)
name_identity.extend(center)
name_identity.extend(right)
print(name_identity)