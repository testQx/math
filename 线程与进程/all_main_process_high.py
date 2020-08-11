import logging
from multiprocessing import Lock, Process
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)
loops = [2, 4]


def run(i, second):
    logging.info("start loop " + str(i) + " at " + ctime())
    sleep(second)
    logging.info("end loop " + str(i) + " at " + ctime())


if __name__ == '__main__':

    logging.info("start all at " + ctime())
    nloops = range(len(loops))
    lock = Lock()
    process = []
    for i in nloops:
        t = Process(target=run, args=(i, loops[i]))
        process.append(t)
    for i in nloops:
        process[i].start()
    for i in nloops:
        process[i].join()
    # for i in nloops:
    #     t.start()
    logging.info("end all at " + ctime())
