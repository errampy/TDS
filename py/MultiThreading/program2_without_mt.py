import time
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
doubles(list_of_number)
squares(list_of_number)
end_time = time.time()

print('TOTAL TIME TAKEN IS : ', end_time - start_time)

"""
    Output:
    double of the 10 is 20
    double of the 20 is 40
    double of the 30 is 60
    double of the 40 is 80
    double of the 50 is 100
    double of the 60 is 120
    square of the 10 is 100
    square of the 20 is 400
    square of the 30 is 900
    square of the 40 is 1600
    square of the 50 is 2500
    square of the 60 is 3600
    TOTAL TIME TAKEN IS :  24.026113510131836

Note : 

same program , done the with threading concept, check the file name : program4_with_mt.py
"""