def find_second_largest_smallest(numbers):
    if len(numbers) < 2:
        return None, None

    
    unique_numbers = sorted(set(numbers))
    
    second_smallest = unique_numbers[1] if len(unique_numbers) > 1 else unique_numbers[0]
    second_largest = unique_numbers[-2] if len(unique_numbers) > 1 else unique_numbers[0]
    
    return second_smallest, second_largest


number_list = [10, 5, 8, 2, 7, 3, 1, 9, 6, 4]
second_smallest, second_largest = find_second_largest_smallest(number_list)

print(f"Second smallest: {second_smallest}")
print(f"Second largest: {second_largest}")