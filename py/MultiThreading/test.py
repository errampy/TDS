import threading

print('Get current thread name ', threading.currentThread().getName())
# output
# Get current thread name  MainThread
'''
doing multiple task simultaneously is called Multi Threading.

There are two types of threading

1. process based multi tasking
    ==> process based multi tasking is best suitable for OS level.
    ==>  there each process is independent task of independent process
2. thread based multi tasking
    ==> it will perform multiple task simultaneously where each task is independent task of the same program 
        is called thread based multi tasking.
'''

