# 双端队列
# 类似与两个栈合并

class Deque():
    def __init__(self):
        self._queue = []

    def add_front(self, item):
        return self._queue.insert(0, item)

    def add_rear(self, item):
        return self._queue.append(item)

    def pop_front(self):
        return self._queue.pop(0)

    def pop_rear(self):
        return self._queue.pop()

    def is_empty(self):
        return self._queue == []

    def size(self):
        return len(self._queue)


if __name__ == '__main__':
    p = Deque()
    p.add_front(1)
    p.add_rear(2)
    # 1 2
    p.add_front(3)
    p.add_rear(4)
    # 3 1 2 4
    print(p.pop_front())
    # 3
    print(p.pop_rear())
    # 4
    print(p.pop_front())
    # 1
    print(p.pop_rear())
    # 2
