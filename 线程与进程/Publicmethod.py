import threading

from loguru import logger


class Publicmethod:

    @staticmethod
    def thread(func):
        threads = []

        # *args在实现函数时正常传参进入
        def thread_loop(count=1):
            try:
                nloops = range(0, count)
                for i in nloops:
                    t = threading.Thread(target=func, args=(i,))
                    # 若t =threading.Thread(target=func,args=(args[0],))
                    # args=(args[0],)需要传值进入被调函数中
                    threads.append(t)
                for i in nloops:
                    threads[i].start()
                    # import time
                    # time.sleep(1)
                for i in nloops:
                    threads[i].join()
            except Exception as e:
                logger.error("count次数输入错误" + e)

        return thread_loop
