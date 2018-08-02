#coding:utf-8

import os
from multiprocessing import Process

'''
# 使用 os 模块中的 fork 方式实现多进程
if __name__ == '__main__':
    print('current Process (%s) start ...' % (os.getpid()))
    pid = os.fork()
    if pid < 0:
        print('error in fork')
    elif pid == 0:
        print('I am child process(%s) and my parent process is (%s)' % (os.getpid(), os.getppid()))
    else:
        # if [,] instead [%], the result number display in the end.
        print('I(%s) created a child process (%s).', (os.getppid(), pid))
'''

#  使用 multiprocessing 模块创建多进程
def run_proc(name):
    print('Child process %s (%s) Running...' % (name, os.getpid()))
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print('Process will start.')
        p.start()
    p.join()
    print('Process end.')