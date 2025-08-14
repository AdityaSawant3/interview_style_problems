# Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

# Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

# Example 1
# Input: arr = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, 1]]

# Example 2
# Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
# Output: [[-6, 6],[-1, 1]]

def two_sum(arr):
    new_arr = []
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] + arr[right] == 0 and arr[left] != 0 and arr[right] != 0:
            if arr[left] < arr[right]:
                new_arr.append([arr[left], arr[right]])
            else:
                new_arr.append([arr[right], arr[left]])
            left += 1
        else:
            right -= 1
    
    return new_arr


# arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
arr = [-1, 0, 1, 2, -1, -4]
answer = two_sum(arr)
print(answer)