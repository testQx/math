class Node(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


def reverseList(head):
    if head == None or head.next == None:  # 若链表为空或者仅一个数就直接返回
        return head
    pre = None
    while (head != None):
        next = head.next  # 1
        head.next = pre  # 2
        pre = head  # 3
        head = next  # 4
        print(pre.elem)
    return pre



if __name__ == '__main__':
    l1 = Node(3)  # 建立链表3->2->1->9->None
    l1.next = Node(2)
    l1.next.next = Node(1)
    l1.next.next.next = Node(9)
    l = reverseList(l1)
    print(l.elem, l.next.elem, l.next.next.elem, l.next.next.next.elem)
