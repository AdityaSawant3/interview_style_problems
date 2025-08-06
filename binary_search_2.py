# Find the max index of the given index.

def binary_search(arr, element):
    arr.sort()
    low = 0
    high = len(arr) - 1
    print(arr)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > element:
            high = mid - 1
        elif arr[mid] < element:
            low = mid + 1
        else:
            result = mid
            low = mid + 1
    return result



arr = [9, 3, 0, 6, -4, -5, 7, 8, 2, 9, 4, 5, 3, 9, 8, 8]
element = 8

index = binary_search(arr, element)

print(f"{element} found at index {index}.")