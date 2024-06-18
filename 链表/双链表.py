class DoubleLinkedNode(object):
    # 初始化结点函数
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    # 初始化头节点函数
    def __init__(self):
        self.head = DoubleLinkedNode(None)

    # 创建双链表函数
    def CreateDoubleLinkedList(self):
        print("请输入数据后按回车键确认，若想结束输入请按“#”。 ")
        cNode = self.head
        data = input("请输入当前结点的值：")
        while data != "#":
            nNode = DoubleLinkedNode(int(data))
            cNode.next=nNode
            nNode.prev=cNode
            cNode=cNode.next
            data = input("请输入当前结点的值：")

    # 判断双链表是否为空
    def IsEmpty(self):
        if self.GetLength() == 0:
            return True
        else:
            return False

    # 判断双链表长度
    def GetLength(self):
        cNode = self.head
        length = 0
        while cNode.next != None:
            length+=1
            cNode=cNode.next
        return length

    # 在表中指定位置插入结点
    def InsertElement(self):
        Pos=0
        cNode = self.head
        iPos = int(input('请输入待插入结点的位置：'))
        while Pos!=iPos:
            pNode=cNode
            cNode=cNode.next
            Pos+=1
        Element=int(input("请输入待插入的值"))
        nNode=DoubleLinkedNode(int(Element))
        nNode.next=cNode
        cNode.prev=nNode
        nNode.prev=pNode
        pNode.next=nNode
        print("结点",Element,"插入成功!")

    # 在表中尾端插入某一结点
    def InsertElementInTail(self):
        Element=int(input("请输入待插入的结点值："))
        if Element == "#":
            return
        cNode=self.head
        nNode = DoubleLinkedNode(int(Element))
        while cNode.next!=None:
            cNode=cNode.next
        cNode.next=nNode
        nNode.prev=cNode
        print("结点", Element, "插入成功！")

    # 删除指定位置的结点
    def DeleteElement(self):
        Pos = 0
        cNode=self.head
        if self.IsEmpty():
            print("当前双链表为空！")
            return
        dPos = int(input("输入要删除的节点位置"))
        while Pos != dPos:
            # 记录删除结点的前一个结点
            qNode = cNode
            Pos+=1
            cNode=cNode.next
        # 表示删除结点的后一个结点
        hNode=cNode.next
        qNode.next=hNode
        hNode.prev = qNode
        del cNode
        print("成功删除第",dPos,"个位置的结点!")

    # 在表中查找指定结点并返回其位置
    def FindElement(self):
        Pos=0
        cNode=self.head
        key = int(input("输入想要查询的结点"))
        if self.IsEmpty():
            print("当前链表为空！")
            return
        while cNode.next!=None and cNode.data!=key:
            cNode=cNode.next
            Pos+=1
        if cNode.data==key:
            print("查找成功！值为", key, "的结点位于该双链表的第", Pos, "个位置")
        else:
            print("查找失败！当前双链表中不存在值为", key, "的元素")

    # 遍历双链表按照prev结点遍历（从后往前）
    def TraverseDoubleLinkedListByPrev(self):
        cNode = self.head
        print("按prev域遍历带头结点双链表：")
        if self.IsEmpty():
            print("当前双链表为空！")
            return
        while cNode.next!=None:
            cNode=cNode.next
        while cNode.prev!=self.head:
            self.VisitElementByPrev(cNode)
            cNode=cNode.prev
        # 输出第一个
        print(cNode.data)

    # 按照prev输出双链表某一元素
    def VisitElementByPrev(self,tNode):
        if tNode!=None:
            print(tNode.data,"->",end=" ")

    # 按照next遍历链表
    def TraverseDoubleLinkedListByNext(self):
        cNode = self.head
        print("按next域遍历带头结点双链表：")
        if self.IsEmpty():
            print("当前链表为空!")
            return
        while cNode.next!=None:
            cNode=cNode.next
            self.VisitElementByNext(cNode)
        print("Node")

    # 按照next输出双链表某一元素
    def VisitElementByNext(self,tNode):
        if tNode.data!=None:
            print(tNode.data,"->",end=" ")

    # 输出函数
    def PrintOut(self):
        print("\n(1)初始化双链表DLL：", end="")
        try:
            self.__init__()
            print("双链表DLL初始化成功！")
        except:
            print("双链表DLL初始化失败")
        print("\n(2)判断当前双链表是否为空：", end="")
        if self.IsEmpty():
            print("当前双链表为空！")
        else:
            print("当前双链表不为空！")
        print("\n(3)创建双链表DLL")
        try:
            self.CreateDoubleLinkedList()
        except ValueError:
            print("输入有误，请重新输入!")
            self.CreateDoubleLinkedList()
        print("\n(4)双链表DLL中元素的个数为", end="")
        try:
            len = self.GetLength()
            print(len)
        except:
            print("获取DLL中结点个数出错！")
        print("\n(5)将值为6的结点插入至DLL中的第3个位置")
        try:
            self.InsertElement()
        except:
            print("插入结点6出错！")
        print("\n(6)在DLL末端插入值为23的结点")
        try:
            self.InsertElementInTail()
        except:
            print("插入结点23出错！")
        print("\n(7)删除DLL中第1个位置的结点")
        try:
            self.DeleteElement()
        except:
            print("删除结点出错！")
        print("\n(8)查找DLL中值为94的结点")
        try:
            self.FindElement()
        except:
            print("查找出错!")
        print("\n(9)按prev域遍历DLL中的所有结点：")
        try:
            self.TraverseDoubleLinkedListByPrev()
        except:
            print("遍历DLL出错!")
        print("\n(10)按next域遍历DLL中的所有结点：")
        try:
            self.TraverseDoubleLinkedListByNext()
        except:
            print("遍历DLL出错!")


if __name__ == '__main__':
    DLL = DoubleLinkedList()
    DLL.PrintOut()