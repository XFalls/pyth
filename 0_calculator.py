import math
a = int(input('a: '))
b = int(input('b: '))
operation = input('+, -, *, /, sin, cos? : ')
if operation == '+':
   print('{} + {} = {}'.format(a, b, a + b))
elif operation == '-':
    print('{} - {} = {}'.format(a, b, a - b))
elif operation == '*':
    print('{} * {} = {}'.format(a, b, a * b))
elif operation == '/':
    print('{} / {} = {}'.format(a, b, a / b))
elif operation == 'sin':
    sin1 = math.sin(a)
    sin2 = math.sin(b)
    print("число а=", (sin1), "число b=", (sin2))
elif operation == 'cos':
    cos1 = math.cos(a)
    cos2 = math.cos(b)
    print("число а=", (cos1), "число b=", (cos2))
else:
    print('this wrong symbol')
