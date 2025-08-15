# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

def search_insert(arr, target):
    
    left = 0
    right = len(arr)-1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return left


nums1 = [1,3,5,6]
target1 = 5
answer1 = search_insert(nums1, target1)
print(answer1)

nums2 = [1,3,5,6]
target2 = 2
answer2 = search_insert(nums2, target2)
print(answer2)

nums3 = [1,3,5,6]
target3 = 7
answer3 = search_insert(nums3, target3)
print(answer3)