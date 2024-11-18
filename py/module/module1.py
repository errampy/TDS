def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


a = 10
b = 20
print('__name__', __name__)
print('module 1')

if __name__ == '__main__':
    print('add ', add(a, b))
    print('sub ', sub(a, b))

print('mul ', mul(a, b))
print('div ', div(a, b))

print('File :- ',__file__)

