# Thread Identification Number(ident):
# -------------------------------------
from threading import *

def test():
    print('chile thread')

t = Thread(target=test)
t.start()
print('Mani thread identification number: ', current_thread().ident)
print('Child Thread identification number: ', t.ident)

"""
Output: 

chile thread
Mani thread identification number:  139897822758720
Child Thread identification number:  139897798461184

"""

# active_count()
# ------------------------
"""
It return the number of active threads currently running
"""
import time
def display():
    print(f'{current_thread().getName()} started')
    time.sleep(3)
    print(f'{current_thread().getName()} ended')
print('The number of active threads: ', active_count())
t1 = Thread(target=display, name="ChildThread1")
t2 = Thread(target=display, name="ChildThread2")
t3 = Thread(target=display, name="ChildThread3")
t1.start()
t2.start()
t3.start()
print('The number of active threads: ', active_count())

time.sleep(5)
print('the number of active threads: ', active_count())

"""
Output: 

The number of active threads:  1
ChildThread1 started
ChildThread2 started
ChildThread3 started
The number of active threads:  4
ChildThread1 ended
ChildThread2 ended
ChildThread3 ended
the number of active threads:  1

"""

# enumerate()
# -------------------------
"""
active_count() : just return the number of active threads(int)
enumerate() : returns the list of all active threads.

"""

def display():
    print(f'{current_thread().getName()} started')
    time.sleep(3)
    print(f'{current_thread().getName()} ended')
t1 = Thread(target=display, name="ChildThread1")
t2 = Thread(target=display, name="ChildThread2")
t3 = Thread(target=display, name="ChildThread3")
t1.start()
t2.start()
t3.start()
print(enumerate())
"""
Output: 
[<_MainThread(MainThread, started 140401232664384)>, <Thread(ChildThread1, started 140401189385984)>, <Thread(ChildThread2, started 140401208366848)>, <Thread(ChildThread3, started 140401199974144)>]

"""

l = enumerate()
print(l)

for t in l:
    print(f'Name : {t.getName()} || identification Number : {t.ident}')

"""
Output:

[<_MainThread(MainThread, started 140534890538816)>, <Thread(ChildThread1, started 140534866241280)>, <Thread(ChildThread2, started 140534847260416)>, <Thread(ChildThread3, started 140534857848576)>]
Name : MainThread || identification Number : 140534890538816
Name : ChildThread1 || identification Number : 140534866241280
Name : ChildThread2 || identification Number : 140534847260416
Name : ChildThread3 || identification Number : 140534857848576
ChildThread3 ended
ChildThread2 ended
ChildThread1 ended

"""


'''
is_alive
'''