from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码
def proc_write(q, urls):
    print('Process(%s) is writing... ' % os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue... ' % url)
        time.sleep(random.random())

# 读取数据执行的代码
def proc_read(q):
    print('Process(%s) is reading... ' % os.getpid())
    while True:
        url = q.get(True)
        print('Get %s from queue.' % url)

if __name__ == '__main__':
    # 父进程创建 Queue，并传给各个子进程
    q = Queue()
    proc_write1 = Process(target=proc_write, args=(q, ['url_1', 'url_2', 'url_3']))
    proc_write2 = Process(target=proc_write, args=(q, ['url_4', 'url_6', 'url_7']))
    proc_reader = Process(target=proc_read, args=(q,))
    # 启动子进程 proc_writer，写入：
    proc_write1.start()
    proc_write2.start()
    # 启动子进程 proc_reader,读取：
    proc_reader.start()
    # 等待 proc_writer 结束
    proc_write1.join()
    proc_write2.join()
    # proc_reader 进程里是死循环，无法等待其结束，只能强行终止
    proc_reader.terminate()

