import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    num_elements = 10  
    min_value = 1     
    max_value = 100    

    random_list = [random.randint(min_value, max_value) for _ in range(num_elements)]
    print("Original list:", random_list)

    bubble_sort(random_list)
    print("Sorted list:", random_list)

if __name__ == "__main__":
    main()