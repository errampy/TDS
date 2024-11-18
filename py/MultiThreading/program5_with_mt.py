# setting and Getting Name Of the Thread:

"""

Every thread in python has some name.

t.getName() ==> Return the name of thread
t.setName() ==> to set out own new name of the thread.

"""

from threading import *

def display():
    print('chile thread', current_thread().getName())

t = Thread(target=display)
t.setName('ChileThreadOfRamMainThread') # setting the custom name of the Child Thread
t.start()

print('Current Thread Name: ', current_thread().getName())
current_thread().setName("RamMainThread") # setting the custom name of the MainThread
print('Current Thread Name: ', current_thread().getName())

'''
Output: 
    
    chile thread ChileThreadOfRamMainThread
    Current Thread Name:  MainThread
    Current Thread Name:  RamMainThread

'''

