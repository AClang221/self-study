"""功能：定义类节点，作用是指向下一结点"""


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = Node


"""定义链表"""


class LinkList:
    def __init__(self, node=None):
        self.__head = node

    """判断链表是否为空"""
    def is_empty(self):
        return self.__head == None

    """求链表长度"""
    def link_list_length(self):
        # cur 游标，用来移动遍历结点
        cur = self.__head
        # count 记录个数
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    """遍历整个链表"""
    def link_list_travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem)
            cur = cur.next
        print()

    """在头部添加数据"""
    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    """在尾部添加数据"""
    def append(self,item):
        node = Node(item)
        if self.is_empty():
           self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    """在指定位置插入元素"""
    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos > self.link_list_length()-1:
            self.append(item)
        else:
            node = Node(item)
            count = 0
            pre = self.__head
            while count < pos-1:
                count +=1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    """删除指定元素"""
    def delete(self,pos):
        pre = self.__head
        count = 0
        while count != pos-1:
            count += 1
            pre = pre.next
        pre_next = pre.next
        pre.next = pre_next.next