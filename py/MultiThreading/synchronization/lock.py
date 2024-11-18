"""
Synchronization by using lock concept:
======================================
The thread will be executed one by one that concepts call synchronization.

creating Lock() object
l = Lock()

l.acquire()
critical section (code)
l.release()
"""

import time
from threading import *
l = Lock()
def wish(name):
    l.acquire() # Thread acquired lock object
    print(f'This Function locked by {current_thread().getName()}')
    for i in range(10):
        print('Good Night ',end='')
        time.sleep(2)
        print(name)
    l.release() #Thread releases lock object.

t1 = Thread(target=wish, args=('Raja',))
t2 = Thread(target=wish, args=('Rani',))
t1.start()
t2.start()