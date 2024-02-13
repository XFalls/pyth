def add(x, y):
    return x + y
def substract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return 'cannot divide by zero'
    else:
        return x / y
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
print('schose operation:')
print('1: add/ 2: subtract/ 3: multiply/ 4: divide')
s = input('Enter your choice: ')
if s in ('1', '2', '3', '4'):
    if s == '1':
        print(add(x, y))
    elif s == '2':
        print(substract(x, y))
    elif s == '3':
        print(multiply(x, y))
    elif s == '4':
        print(divide(x, y))
else:
    print('invalid')