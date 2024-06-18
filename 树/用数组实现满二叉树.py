"""
二叉树：是树形结构，其特点为，它的每个结点都有两个分支，称为左右子树，因此二叉树最大的度就是2，左节点小于右节点
"""
# 此处的二叉树为满二叉树
def Binary_tree_craet(tree_array,data,length):
    for i in range(1,length):
        ind=1
        while tree_array[ind] != 0:
            if data[i] > tree_array[ind]:
                ind = ind * 2 + 1
            else:
                ind = ind * 2
        tree_array[ind] = data[i]


# lenght表示树的结点个数，data表示各个结点的值，tree_array表示二叉树用列表表示的结果
length = 9
data = [0,3,2,6,7,4,5,1,9]
tree_array = [0] * 16
Binary_tree_craet(tree_array, data, 9)
for i in range(1,16):
    print(tree_array[i],end=" ")