Map=[input() for i in range(4)]
s=set()
for i in range(4):
    # 取第i行的前三个
    s.add(Map[i][:3])
    # 取第i行的后三个
    s.add(Map[i][1:])
    # 取第i列的前三个
    s.add(Map[0][i]+Map[1][i]+Map[2][i])
    # 取第i列的后三个
    s.add(Map[1][i]+Map[2][i]+Map[3][i])
for i in range(2):
    for j in range(2):
        # 取斜着方向上的三个点
        s.add(Map[i][j]+Map[i+1][j+1]+Map[i+2][j+2])
        s.add(Map[i][j+2]+Map[i+1][j+1]+Map[i+2][j])
# 判断加入集合中的图是否存在以下三种情况
print("YES" if {"x.x",".xx","xx."}&s else "NO")