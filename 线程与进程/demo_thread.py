# class Test():
#     @staticmethod
#     def wrapper(func):
#         def f():
#             print('在wrapper中执行func前')
#             func()
#             print('在wrapper中执行func后')
#         return f
#
# @Test.wrapper
# def fengshan():
#     print('出风')
#
# fengshan()
from 线程与进程.Publicmethod import Publicmethod


@Publicmethod.thread
def fengshan(i):
    # 若threading.Thread(target=func,args=(args[0],))
    # 则该处fengshan()需更改为 fengshan(loops)需要接收参数
    print('出风')


if __name__ == '__main__':
    fengshan(count=4)
# [1,2,3,4]进入thread中的*arg中

'''>>>
    出风
    出风
    出风
    出风'''
