"""
Daemon Threads:
----------------
Daemon  ---> Ghost

The threads which are running in the background is called Daemon threads.

eg :
    garbage collector

Main purpose of daemon threads:

    To provide support for non-daemon thread like main thread.

how to check whether thread is daemon or not
t.isDaemon()
t.daemon

"""
import time
from threading import *

def check_daemon():
    print(current_thread().isDaemon())  # False
    print(current_thread().daemon)  # False

# check_daemon()

def change_to_daemon():
    current_thread().setDaemon(True) # RuntimeError: cannot set daemon status of active thread
    print(current_thread().isDaemon())

# change_to_daemon()
"""
MainThread is always Non-Daemon.
"""

"""
Default nature : 
-----------------
Main Thread is always Non-Daemon.
by default, The Daemon nature of remaining threads will be inherited from the parent thread.
"""
def display():
    print('hello')

t = Thread(target=display) # Parent thread of t is MainThread
print(t.isDaemon())# False
t.setDaemon(True)
print(t.isDaemon()) # True

"""
If the parent is non-daemon then child is also non-daemon by default
If the parent is daemon then child is also daemon by default
"""

def display2():
    print('display2')

def display1():
    print('display 1')
    t2 = Thread(target=display2)
    print(f't2 Threads : {t2.daemon}')

t1 = Thread(target=display1)
print(f't1 Thread : {t1.isDaemon()}')
t1.setDaemon(True)
print(f't1 Thread : {t1.isDaemon()}')
t1.start()

time.sleep(10)
print('End Main Threads')