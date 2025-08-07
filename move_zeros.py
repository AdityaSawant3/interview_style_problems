# Input: [0, 1, 9, 0, 4, 0, 7]
# Output: [1, 9, 4, 7, 0, 0, 0]

def move_zeros(arr):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == 0:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


arr = [0, 1, 9, 0, 4, 0, 7, 9, 0, 3, 5, 0, 2]
another_arr = move_zeros(arr)
print(another_arr)
