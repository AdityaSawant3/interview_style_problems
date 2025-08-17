# Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.

# Examples:

# Input: a[] = [1, 2, 5, 4, 0], b[] = [2, 4, 5, 0, 1]
# Output: true
# Explanation: Both the array can be rearranged to [0,1,2,4,5]
# Input: a[] = [1, 2, 5], b[] = [2, 4, 15]
# Output: false
# Explanation: a[] and b[] have only one common value.

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(n)

def checkEqual(a, b) -> bool:
    
    another_a = mergeSort(a)
    another_b = mergeSort(b)
    
    return another_a == another_b
    
def mergeSort(b):
    
    if len(b) > 1:
        
        left_arr = b[:len(b)//2]
        right_arr = b[len(b)//2:]
        
        mergeSort(left_arr)
        mergeSort(right_arr)
        
        i = j = k = 0
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                b[k] = left_arr[i]
                i += 1
            else:
                b[k] = right_arr[j]
                j += 1
            k += 1
            
        while i < len(left_arr):
            b[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            b[k] = right_arr[j]
            j += 1
            k += 1
            
        return b


a = [1, 2, 5, 4, 0]
b = [2, 4, 5, 0, 1]
answer = checkEqual(a, b)
print(answer)
