def two_pointer(arr, target):

    new_arr = []
    left = 0
    right = len(arr)-1

    while left < right:
        if arr[left] + arr[right] == target:
            if arr[left] < arr[right]:
                new_arr.append([arr[left], arr[right]])
            else:
                new_arr.append([arr[right], arr[left]])
            return new_arr
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            left += 1
        
    return new_arr



arr = [-3, -1, 0, 1, 2]
target = -2

answer = two_pointer(arr, target)
print(f"Answer is {answer}")