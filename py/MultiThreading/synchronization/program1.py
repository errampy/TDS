"""
Synchronization
--------------------
If multiple threads are operation simultaneously,
then there may be change of data inconsistency problem(Race Condition).
to prevent this problem we should go for synchronization concepts.

"""
import time
from threading import *
def wish(name):
    for i in range(10):
        print('Good Night ',end='')
        time.sleep(2)
        print(name)

t1 = Thread(target=wish, args=('Raja',))
t2 = Thread(target=wish, args=('Rani',))
t1.start()
t2.start()

"""
Output: 

-DS-VAMSI-KRISHNA-SIR/python/MultiTreading/synchronization$ python program1.py
Good Night Good Night Raja
Good Night Rani
Good Night Raja
Rani
Good Night Good Night Raja
Rani
Good Night Good Night Raja
Rani
Good Night Good Night Raja
Good Night Rani
Good Night Raja
Good Night Rani
Good Night Raja
Rani
Good Night Good Night Rani
Raja
Good Night Good Night Rani
Good Night Raja
Good Night Rani
Raja


here, we are seeing data inconsistency problem
"""