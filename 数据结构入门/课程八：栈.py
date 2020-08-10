# 后进先出
'''
栈：描述数据操作
（可以通过链表（删除添加/删除的某些方法，固定只能从尾部添加，尾部移除），顺序表（规定进出规则）实现）
线性表描述数据如何存放
'''


class stack():
    '''
    栈
    顶部栈顶，底部栈底
        push(item) 入栈/压栈，添加一个新的元素到栈顶
        pop() 出栈，弹出顶元素
        peek() 返回栈顶元素
        is_empty() 判断栈是否为空
        size() 返回栈的元素
        '''
    def __init__(self):
        #建立容器
        self._list=[]

    def push(self,item):
        self._list.append(item)
        #self._list.insert(0,item)

    def pop(self):
        return self._list.pop()
        #self._list.pop(0)

    def peek(self):
        if self._list:
            return self._list[-1]
        else:
            return None

    def is_empty(self):
        return self._list == []
        #或者 return not self._list
        # 0 {} [] ""  这些在逻辑值中均为假

    def size(self):
        return len(self._list)

if __name__ == '__main__':
    s=stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
