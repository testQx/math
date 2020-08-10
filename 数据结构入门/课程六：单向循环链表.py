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


class Node(object):
    '''结点'''

    def __init__(self, elem):
        # 节点对象的两个属性
        self.elem = elem
        self.next = None

    '''定义链表的数据结构'''


class SingleCycleLinkList(object):
    '''单向循环链表'''

    def __init__(self, node=None):

        self._head = node
        # 存在node时，尾节点需重新指回头节点
        if node:
            node.next = node

    def is_empty(self):
        '''链表是否为空'''
        return self._head == None

    def length(self):
        ''''链表长度'''
        # cur游标（指针），用来移动遍历节点
        # cur别名 指向self._head这个别名对应的存储地址（对象数据）
        if self.is_empty():
            return 0
        cur = self._head

        # 当尾节点指回头节点时，满足while条件，导致count未+1，所以此处count需从1开始
        count = 1
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环，cur指向尾节点，但为节点的元素未打印，需要手动打印出来
        print(cur.elem)
        print("\n")  # 进行换行

    def add(self, item):
        '''链表头部添加元素'''
        node = Node(item)
        cur = self._head
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            node.next = self._head
            while cur.next != self._head:
                # 此时指向尾节点
                cur = cur.next
            node.next = self._head
            self._head = node
            # 操作尾节点重新指向新添加头节点后的头节点
            cur.next = node
            #  或者cur.next = self._head

    def append(self, item):
        '''链表尾部添加元素，尾插法'''
        # 此时的item指明的是具体数值，而非节点
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            # 当特殊情况时，空链表，cur=None，走下方条件cur.next时报错，需要添加新的判断
            while cur.next != self._head:
                # node.next = cur.next
                # cur.next = node
                cur = cur.next
            node.next = self._head
            cur.next = node

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
            pre = self._head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        '''删除节点'''
        if self.is_empty():
            return
        cur = self._head
        pre = None
        while cur.next != self._head:
            if cur.elem == item:
                if cur == self._head:
                    # 头节点
                    # 先找尾节点
                    rear = self._head
                    while rear.next != self._head:
                        rear = rear.next
                    self._head = cur.next
                    rear.next = self._head
                    # rear.next = cur.next
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:
            if cur == self._head:
                # if cur.next == self._head:
                # 尾节点只有一个
                self._head = None
            else:
                # 尾节点含有多个
                pre.next = cur.next

    def search(self, item):
        '''查找节点是否存在'''
        cur = self._head
        if self.is_empty():
            return False
        while cur != self._head:
            # 此处while条件同上length()
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False
        # 整体编写完后，需要考虑一种特殊情况-》空链表，此时将值从新代入

    def reverse(self):
        if self._head == None or self._head.next == None:
            print(self._head)
        else:
            pre = None
            cur = self._head  # 抽象为头节点
            while cur != None:
                next = cur.next
                # 设置next等于第二个节点的地址
                cur.next = pre
                # 设置第一个节点指向None（循环后指上一个节点）
                pre = cur
                # 设置pre节点指向原先的第一个节点（上一个节点）
                cur = next
                # 设置头节点指向第二个节点
            while pre != None:
                print(pre.elem, end=" ")
                pre = pre.next


if __name__ == "__main__":
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.travel()
    ll.remove(1)
    ll.travel()
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
