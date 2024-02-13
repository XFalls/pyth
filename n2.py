def print_first_ten_primes():
    count = 0
    number = 2
    while count < 10:
        if is_prime(number):
            print(number)
            count += 1
        number += 1

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print_first_ten_primes()