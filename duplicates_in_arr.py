# Find duplicate number in the array.

def find_duplicate(arr):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[j]
                


arr = [6, 2, 4, 8, 9, 12, 23, 45, 67, 12]
duplicate_num = find_duplicate(arr)
print(f"Duplicate number found: {duplicate_num}")