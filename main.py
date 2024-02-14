from utils.py import factorial

num=int(imput())
print(factorial(num))


from utils.py import find_gcd

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

gcd = find_gcd(num1, num2)

print(f"НСД({num1}, {num2}) = {gcd}

from utils.py import  simple

num = int(input())
if simple(num):
    print("є простим числом")
else:
    print("не є простим числом")
