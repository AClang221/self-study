# 创建树的结点
class Tree:
    def __init__(self):
        self.data=0
        self.left=None
        self.right=None



def Creat_tree(root,value):  # root表示根节点，value节点值
    new_node = Tree()       # 创建树结点
    new_node.data=value     # 数据域
    new_node.left=None      # 左子树
    new_node.right=None     # 右子树
    if root==None:          # 如果根节点为空，这种情况是空二叉树
        root=new_node       # 将当前结点定义为根节点
        return root
    else:
        current=root        # 因为要进行结点的添加所以将current赋值成根节点进行操作防止根节点丢失
        while current!=None:
            backup=current  # 因为到最后current表示的肯定是一个空结点，这样才能在空结点上进行结点的添加，所以要用当前值value
                            # 与当前的  "父节点"  进行比较，然后决定放在左右子树的其中一边，backup用来出存放这个  ""父节点""
            if current.data>value:  # 根节点大于当前值
                current=current.left    # 将该节点放在左子树上
            else:
                current=current.right
        if backup.data>value:   # 判断将该节点放在左子树还是右子树
            backup.left=new_node
        else:
            backup.right=new_node
    return root


# 输入节点值
root=Creat_tree(None,3)
for i in range(7):
    Creat_tree(root,int(input()))


# 前序遍历
def preorder(tree):
    if tree==None:
        return
    print(tree.data,end=" ")
    preorder(tree.left)
    preorder(tree.right)
preorder(root)
print()

# 中序遍历
def inorder(tree):
    if tree==None:
        return
    inorder(tree.left)
    print(tree.data,end=" ")
    inorder(tree.right)
inorder(root)
print()
# 后序遍历
def postorder(tree):
    if tree==None:
        return
    postorder(tree.left)
    postorder(tree.right)
    print(tree.data,end=" ")
postorder(root)
