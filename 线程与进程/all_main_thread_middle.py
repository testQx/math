import _thread
import logging
from time import sleep,ctime
logging.basicConfig(level=logging.INFO)

loops=[2,4]
def loop(nloop,nsec,lock):
    logging.info("start loop"+str(nloop)+" at "+ctime())
    sleep(nsec)
    logging.info("end loop "+str(nloop)+" at " + ctime())
    lock.release()

def main():
    logging.info("start all at "+ctime())
    locks=[]
    nloops=range(len(loops))
    for i in nloops:
        lock =_thread.allocate_lock()#声明一个锁
        lock.acquire() #加锁
        locks.append(lock)
    # 分开写for i in nloops：因为加锁需要时间，若第一个线程已结束，则通过了locks.locked()的判断，会造成解锁
    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked():
            pass
    logging.info("end all at "+ctime())

main()