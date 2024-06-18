class Node(object):
    # 初始化节点函数
    def __init__(self,data):
        self.data = data
        self.next = None


class SingleLinkedList(object):
    # 初始化头节点函数
    def __init__(self):
        self.head = Node(None)

    # 创建单链表函数
    def CreateSingleLinkedList(self):
        print("-------------------------")
        print("请输入数据后按回车确认，若要结束输入#")
        print("-------------------------")
        # 单链表
        cNode=self.head
        # 要添加的元素
        Element = input("请输入当前节点的值：")
        while Element!="#":
            # 新添加的结点
            nNode = Node(int(Element))
            cNode.next=nNode
            cNode=cNode.next
            Element = input("请输入当前节点的值：")
        print("单链表创建完毕")

    # 判断链表是否为空
    def IsEmpty(self):
        if self.GetLength()==0:
            return True
        else:
            return False


    # 判断链表长度
    def GetLength(self):
        # 将cNode定义为头结点
        cNode=self.head
        # 记录长度
        leigth=0
        # 一直遍历到下一个节点为空
        while cNode.next!=None:
            leigth+=1
            cNode=cNode.next
        return leigth

    # 在链表中指定位置插入结点
    def InsertElement(self):
        Pos=0
        # cNode定义为头结点
        cNode = self.head
        iPos=int(input("输入待插入结点的位置"))
        while Pos<iPos-1:
            cNode=cNode.next
            Pos+=1
        Element = int(input("输入要插入的数据"))
        nNode=Node(int(Element))
        nNode.next=cNode.next
        cNode.next=nNode
        print("结点",Element,"插入成功")


    # 在链表头部插入某一结点
    def InsertElementInHead(self):
        Element=int(input("输入要插入的结点"))
        if Element=="#":
            return
        cNode=self.head
        nNode=Node(int(Element))
        nNode.next=cNode.next
        cNode.next=nNode
        print("结点",Element,"插入完毕")

    # 删除指定位置结点
    def DeleteElement(self):
        Pos=0
        cNode=self.head
        if self.IsEmpty():
            print("当前链表为空")
            return
        dPos = int(input("输入要删除的结点"))
        while Pos<dPos-1:
            cNode=cNode.next
            Pos += 1
        pNode = cNode
        cNode = cNode.next
        pNode.next = cNode.next
        del cNode
        print("成功删除第", dPos, "个位置的结点！")


    # 查询某一结点
    def FindElement(self):
        Pos = 0
        cNode=self.head
        sPos=int(input("输入要查询的"))
        while Pos<sPos:
            cNode=cNode.next
            Pos+=1
        key=cNode.data
        print("查找成功！第", Pos, "个位置的结点值为", key)


    # 遍历单链表函数
    def TraverseElement(self):
        cNode = self.head
        if cNode.next==None:
            print("当前单链表为空")
            return
        print("您当前的单链表为：")
        while cNode!=None:
            cNode=cNode.next
            self.VisitElement(cNode)


    # 输出单链表某一元素
    def VisitElement(self,tNode):
        if tNode!=None:
            print(tNode.data,"->",end="")
        else:
            print("None")


    # 定义输出函数
    def PrintOut(self):
        print("*****************************************************")
        print("***********基础实验2  实现单链表的基础操作***********")
        print("\n(1)初始化单链表SLL仔：", end="")
        try:
            self.__init__()
            print("单链表SLL初始化成功！")
        except:
            print("单链表SLL初始化失败")
        print("\n(2)判断当前单链表是否为空：", end="")
        if self.IsEmpty():
            print("当前链表为空！")
        else:
            print("当前链表不为空！")
        print("\n(3)创建单链表SLL")
        try:
            self.CreateSingleLinkedList()
        except ValueError:
            print("输入有误，请重新输入!")
            self.CreateSingleLinkedList()
        print("\n(4)单链表SLL中元素的个数为", end="")
        try:
            sum = self.GetLength()
            print(sum)
        except:
            print("获取SLL中结点个数出错！")
        print("\n(5)将值为11 的结点插入至SLL中的第3个位置")
        try:
            self.InsertElement()
        except:
            print("插入结点11出错！")
        print("\n(6)在SLL首端插入值为25的结点")
        try:
            self.InsertElementInHead()
        except:
            print("插入结点25出错！")
        print("\n(7)删除SLL中第4个位置的结点")
        try:
            self.DeleteElement()
        except:
            print("删除结点出错！")
        print("\n(8)查找SLL中第3个位置结点的值")
        try:
            self.FindElement()
        except:
            print("查找出错!")
        print("\n(9)遍历SLL中的所有结点：")
        try:
            self.TraverseElement()
        except:
            print("遍历SLL出错!")


if __name__=='__main__':
    SLL=SingleLinkedList()
    SLL.PrintOut()
