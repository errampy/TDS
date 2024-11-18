import time
from threading import *
def doubles(numbers):
    for n in numbers:
        time.sleep(2)
        print(f'double of the {n} is {n*2}')

def squares(numbers):
    for n in numbers:
        time.sleep(2)
        print(f'square of the {n} is {n*n}')

list_of_number = [10, 20, 30, 40, 50, 60]
start_time = time.time()

t1 = Thread(target=doubles, args=(list_of_number,))
t2 = Thread(target=squares, args=(list_of_number,))
t1.start()
t2.start()
t1.join() # this means , wait don't execute main thread until finished the t1
# after completing t1 only main thread will continue its execution
t2.join() # this means , wait don't execute main thread until finished the t1
# after completing t2 only main thread will continue its execution
end_time = time.time()

print('TOTAL TIME TAKEN IS : ', end_time - start_time)

"""
    Output:
    double of the 10 is 20
    square of the 10 is 100
    square of the 20 is 400
    double of the 20 is 40
    square of the 30 is 900
    double of the 30 is 60
    double of the 40 is 80
    square of the 40 is 1600
    square of the 50 is 2500
    double of the 50 is 100
    square of the 60 is 3600
    double of the 60 is 120
    TOTAL TIME TAKEN IS :  12.013314247131348
    
Note : same program written  without threading concept check file name : program2_without_mt.py file.

If jobs are independent then highly recommended to go for thread concept
"""
