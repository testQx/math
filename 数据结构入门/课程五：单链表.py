# 单链表操作

'''
数据结构：指一个对象+对象具体的方法构成
对于节点而言：
Class Node():
elem
Next

node1: elem=10  next=node2
node2: elem=20  next
'''
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
    # node =Node(100)
    # node1 =Node(200)
    # 每一个node节点，都需要Node这个对象
    # 或者利用python的特殊性，封装为（elem,next）的元组
    # 为了适应其他语言，统一进行构造
    '''结点'''

    def __init__(self, elem):
        # 节点对象的两个属性
        self.elem = elem
        self.next = None

    '''定义链表的数据结构'''


class SingleLinkList(object):
    '''单链表'''

    def __init__(self, node=None):
        # 用户先定义了一个node=Node(100)这个节点
        # 然后将这个节点给到链表头去指向 则这里的node参数就指向了这个节点（elem+next）
        # node = None 默认值 创建一个空链表
        # 私有属性，对外不暴露，加下划线，仅供内部函数调用
        self._head = node

    def is_empty(self):
        '''链表是否为空'''
        return self._head == None

    def length(self):
        ''''链表长度'''
        # cur游标（指针），用来移动遍历节点
        # cur别名 指向self._head这个别名对应的存储地址（对象数据）
        cur = self._head
        # count用来记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
        # while条件可以由两种构成
        # 游标cur 指向一个完整节点（elem + next）
        # （1）cur.next == None (通过节点的next执行None判断)
        # 采用这种条件，count会少算一次，在最后一次游标记录时，cur.next==None未进入循环体，导致count没有再次+1
        # 若是采用这种条件，则count初始值需为1，才能避免漏数一次
        # 且最后判断特殊条件（空链表）时，需返回count=0
        # (2) cur == None （通过整个节点为None判断）
        # 若是采用这种条件，则count初始值需为0
        # 整体编写完后，需要考虑一种特殊情况-》空链表，此时将值从新代入，cur == self.head == None

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
        # 将新插入的节点的next指向现在self._head别名内存对应的存储地址（对象数据）
        self._head = node
        # 把原本的头指向最新的node节点
        # 整体编写完后，需要考虑一种特殊情况-》空链表，此时将值从新代入

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
        cur = self._head
        pre = None
        count = 0
        while cur != None:
            if cur.elem == item:
                # 特殊情况：先判断此节点是否是头节点
                # 判断是否是头节点：cur==self._head或者pre=None
                # 特殊情况：只有一个节点，删除节点则self._head=None
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
            count += 1
        # 获取删除节点的下标
        print("删除节点的下标为:", count)

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

    def reverse(self):
        if self._head==None or self._head.next==None:
            print(self._head)
        else:
            pre = None
            cur = self._head#抽象为头节点
            while cur != None:
                next = cur.next
                #设置next等于第二个节点的地址
                cur.next = pre
                #设置第一个节点指向None（循环后指上一个节点）
                pre = cur
                # 设置pre节点指向原先的第一个节点（上一个节点）
                cur = next
                # 设置头节点指向第二个节点
            while pre!=None:
                print(pre.elem,end=" ")
                pre=pre.next




if __name__ == "__main__":
    ll = SingleLinkList()
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
    ll.reverse()


