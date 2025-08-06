def binary_search(arr, element):
    arr.sort()
    low = 0
    high = len(arr)-1
    print(arr)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            high = mid - 1
        else:
            low = mid + 1



arr = [9, 3, 0, 6, -4, -5, 7, 8, 2, 9, 4, 5, 3, 9]
element = 8
index = binary_search(arr, element)
print(f"{element} found at index {index}.")