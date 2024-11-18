# 3. Creating a thread without extending Thread class

from threading import *

class Test:
    def display(self):
        for i in range(10):
            print('How is going on? ')

obj = Test()
t = Thread(target=obj.display)
t.start()
for i in range(10):
    print('Hope, you enjoying this concept')

'''
We can't start same thread multiple time, we will get runtime error.

'''