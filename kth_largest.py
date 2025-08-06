# Find the kth largest element from the array

def find_largest(arr, num):
    k = 1
    for i in range(len(arr)):
        if arr[i] < num:
            k += 1
    return k
arr = [3, 1, 5, 12, 2, 11]
num = 5

kth = find_largest(arr, num)
print(f"{num} is {kth} largest number.")