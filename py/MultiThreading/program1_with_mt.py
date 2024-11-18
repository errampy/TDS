"""
There are a multiple way to creating the Thread
1. creating  a thread without using any class
2. creating a thread by extending Thread class
3. creating a thread without extending Thread class
"""

from threading import *
# 1. creating  a thread without using any class

def display():
    for i in range(10):
        print('Ram :- Executed By ', current_thread().getName())

def display1(name):
    for i in range(10):
        print(f'{name} :- Executed By ', current_thread().getName())

t = Thread(target=display)
t1 = Thread(target=display1, args=('Mohan',))
t.start()
t1.start()

for j in range(10):
    print('Mantu :- Executed By ', current_thread().getName())

'''
This is sample program written based on thread,
in the program we have two tread,
    1. MainThread
    2. Thread-1
    
    display function will run as child Thread, called Thread-1
    and remaining will run as MainThread
'''

