def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_and_print_primes(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num)

limit = int(input("Enter a number: "))
find_and_print_primes(limit)