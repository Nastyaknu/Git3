def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def simple(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a



def check_even_odd(number):
    if number % 2 == 0:
        return "Парне число"
    else:
        return "Непарне число"
result = check_even_odd(num)
print(f"{num} - {result}")
