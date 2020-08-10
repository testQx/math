# 先进先出
'''
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
'''


class Queue:
    '''队列
    左侧队头，右侧队尾'''

    def __init__(self):
        self._queue = []

    def enqueue(self, item):
        return self._queue.append(item)
        # return self._queue.insert(0,item)

    def dequeue(self):
        return self._queue.pop(0)
        # return self._queue.pop

    # 出队/入队总有一个时间复杂度为O(n),另一个为O(1)
    # 根据使用频繁情况来决定参用哪种方式
    # 例如 return self._queue.append(item) 说明尾部O(1)
    # 此时对应的 return self._queue.pop(0) 为O(n)

    def is_empty(self):
        return self._queue == []

    def size(self):
        return len(self._queue)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
