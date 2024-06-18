"""定义一个结点"""


class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


    """定义一个链表"""


class SingleLink:
    def __init__(self):
        self.__head = Node()


    """判断链表元素是否为空"""


    def is_empty(self):
        return self.__head.next is None


    """在末尾添加元素"""


    def append(self, item):
        node = Node(item)
        cur = self.__head
        while cur.next:
            cur = cur.next
        cur.next = node


    """查找元素是否在链表中"""


    def find(self, item):
        cur = self.__head
        ans = 0
        while cur:
            ans += 1
            if cur.item == item:
                return print("YES")
            else:
                cur = cur.next
        return print("NO")


    """判断链表的长度"""


    def SingleLink_length(self):
        count = 0
        sur = self.__head.next
        while sur:
            sur = sur.next
            count += 1
        return count


    """将元素插入链表中对应位置"""


    def insert(self, pos, item):
        if pos == 1:
            node = Node(item)
            node.next = self.__head.next
            Link_list.print()
            self.__head.next = node
            Link_list.print()
        elif pos > self.SingleLink_length():
            self.append(item)
        else:
            count = 0
            node = Node(item)
            pre = self.__head
            while count < pos - 1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node


    """删除链表的指定元素"""


    def delete(self, pos):
        pre = self.__head
        count = 0
        while count != pos - 1:
            count += 1
            pre = pre.next
        pre_next = pre.next
        pre.next = pre_next.next

    """顺序打印链表"""
    def print(self):
        cur = self.__head.next
        while cur:
            print(cur.item,end="->")
            cur = cur .next
        print("Node")

n = int(input())
Link_list = SingleLink()
for i in range(n):
    lst = list(map(int,input().split()))
    if lst[0] == 1:
        Link_list.append(lst[1])
        Link_list.print()
    elif lst[0] == 2:
        Link_list.find(lst[1])
        Link_list.print()
    elif lst[0] == 3:
        Link_list.insert(lst[1],lst[2])
        Link_list.print()
    elif lst[0] == 4:
        Link_list.delete(lst[1])
        Link_list.print()
    else:
        print("输入有误")
