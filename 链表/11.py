"""下标值从1开始计数是一个好习惯"""
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

    """查找元素是否在链表中，如果存在，返回下表，不存在，返回-1"""

    def find(self, item):
        cur = self.__head.next
        ans = 0
        while cur:
            ans += 1
            if cur.item == item:
                break
            else:
                cur = cur.next
        return ans if ans else -1

    """判断链表的长度"""
    def SingleLinkLength(self):
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
            self.__head.next = node
        elif pos > self.SingleLinkLength():
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
        while count != pos-1:
            count += 1
            pre = pre.next
        pre_next = pre.next
        pre.next = pre_next.next

    """顺序打印链表"""
    def print(self):
        cur = self.__head.next
        while cur:
            print(cur.item,end='->')
            cur = cur.next
        print("None")


sl = SingleLink()
arr = [1,2,3,4,5,6,7]
for i in arr:
    sl.append(i)
sl.print()
print(sl.find(5))
sl.append(8)
sl.insert(1,9)
sl.print()
sl.insert(2,10)
sl.delete(8)
sl.print()