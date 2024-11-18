# 2. creating  a thread by extending Thread class
"""
Extending Thread class means we have to create the child class For the Tread class.
We have to override/define run() method with our required job.


"""
from threading import *

class MyThread(Thread):
    def run(self):
        # here need to define all the task.
        for i in range(10):
            print('Good morning : Durga Sir')

mt = MyThread() # Main Thread creating Child thread object
mt.start() # Main Thread starts child thread

for j in range(10):
    print('Good morning : Ram')
