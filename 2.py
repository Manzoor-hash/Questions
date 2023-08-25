numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sum_numbers(numbers):
    even = 0
    for num in numbers:
        if num % 2 == 0:
            even += num
    return even

result = sum_numbers(numbers)
print("Sum of even numbers:", result)