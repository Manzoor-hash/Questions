# Write a Python program to calculate the factorial of a given number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)  
num = int(input("Enter a number: "))
if num < 0:
        print("Error: ")
else:
        result = factorial(num)
        print(f"Factorial of {num} is {result}")