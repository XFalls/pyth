num = int(input('Write count even numbers: '))
def first_even():
    count = 0
    number = 2
    while count < num:
        if is_even(number):
            print(number)
            count += 1
        number += 1

def is_even(number):
    if number % 2:
        return False
    return True
print(first_even())
