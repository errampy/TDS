"""
join() method:

if a thread wats to wait until completing some other thread ,
then we should go for join() method.

for example
==============
marraige related
----------------

1. value fixing
2. wedding card printing
3. wedding cards distribution



"""

from threading import  *

import time
def display():
    for i in range(10):
        print('ram thread')
        time.sleep(3)
t = Thread(target=display)
t.start()
# t.join() # Main thread will wait until completing child thread
t.join(10) # Main thread will wait until completing child thread or max 10 seconds
for i in range(10):
    print('mantu thread')

"""
you are waiting for your friend.

How much time you will wait??
    option 1 : until my friend is coming(t.join())
    option 2 : until my friend is coming or 1 hour max (t.join(1 hour))
"""
"""
till now  , what we discussed

how many ways to define the thread
getting and setting of name of thread
thread identification number
active_count()
enumerate()
is_alive()
join()

"""