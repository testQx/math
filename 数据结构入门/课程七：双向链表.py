'''
对于链表而言：
Class SingleLinkList():
is.empty() 链表是否为空
length() 链表长度
travel（） 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos,item) 链表指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在
'''


# 定义节点
class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinklist(object):

    def __init__(self, node=None):
        # 指向头节点
        self._head = node

    def is_empty(self):
        '''链表是否为空'''
        return self._head is None

    def length(self):
        ''''链表长度'''
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self._head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("\n")  # 进行换行

    def add(self, item):
        pass
        '''链表头部添加元素'''
        node = Node(item)
        node.next = self._head
        self._head = node
        node.next.prev = node
        # 或者后2行改成
        # self._head.prev=node
        # self._head=node

    def append(self, item):
        '''链表尾部添加元素，尾插法'''
        # 此时的item指明的是具体数值，而非节点
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            # 当特殊情况时，空链表，cur=None，走下方条件cur.next时报错，需要添加新的判断
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        '''链表指定位置添加元素
        :param pos 从0开始
        '''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            # 这里不可以pos =(self.length()-1)，相当于在指定位置插入元素
            self.append(item)
        else:
            cur = self._head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        '''删除节点'''
        cur = self._head
        while cur != None:
            if cur.elem == item:
                if cur == self._head:
                    self._head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        '''查找节点是否存在'''
        cur = self._head
        while cur != None:
            # 此处while条件同上length()
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
        # 整体编写完后，需要考虑一种特殊情况-》空链表，此时将值从新代入


if __name__ == '__main__':
    ll = DoubleLinklist()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    # 8 1 2 3 4 5
    ll.insert(-1, 9)
    ll.travel()
    # 9 8 1 2 3 4 5
    ll.insert(2, 100)
    ll.travel()
    # 9 8 100 1 2 3 4 5
    ll.insert(9, 200)
    ll.travel()
    # 9 8 100 1 2 3 4 5 200
    ll.remove(100)
    ll.travel()
    # 删除节点的下标为: 2
    # 9 8 1 2 3 4 5 200
    ll.remove(9)
    ll.travel()
    # 删除节点的下标为: 0
    # 8 1 2 3 4 5 200
    ll.remove(200)
    ll.travel()
    # 删除节点的下标为: 6
    # 8 1 2 3 4 5
