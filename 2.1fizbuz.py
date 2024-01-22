a = int(input('введи число : '))
if a % 3 == 0 and a % 5 == 0:
    print('FizBuz')
elif a % 3 == 0:
    print('Buz')
elif a % 5 == 0:
    print('Fiz')