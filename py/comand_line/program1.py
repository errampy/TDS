"""
COMMAND LINE ARGUMENT :
it is process the take argument while running the file

by using sys module we can get the command line arguments.

command line argument, argument must be separate by space only line else it will consider as single argument only

argv : type of argv is list always, and at the 0 always should be file name itself
"""
from sys import argv
print('here Im practicing command line argument...')
print('Argument Provided : ',argv)

print('type of argv ', type(argv))
# read argument from command line argument and do the sum
sum = 0
for data in argv:
    if data.isdigit():
        sum+=eval(data)

print("sum ",sum)

"""
:output
 withoud passing any argument
$ python program1.py

here Im practicing command line argument...
Argument Provided :  ['program1.py']
type of argv  <class 'list'>
sum  0


here Im practicing command line argument...
Argument Provided :  ['program1.py']
type of argv  <class 'list'>
sum  0


passing some of the argument.

$ python program1.py 10 10 'ram' 'sadf' iuwerui 34

here Im practicing command line argument...
Argument Provided :  ['program1.py', '10', '10', 'ram', 'sadf', 'iuwerui', '34']
type of argv  <class 'list'>
sum  54

"""