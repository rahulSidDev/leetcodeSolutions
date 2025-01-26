# Background

## How does it work?

In its simplest form, Binary Search operates on a contiguous sequence with a specified left and right index. This is called the Search Space. Binary Search maintains the left, right, and middle indicies of the search space and compares the search target or applies the search condition to the middle value of the collection; if the condition is unsatisfied or values unequal, the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful. If the search ends with an empty half, the condition cannot be fulfilled and target is not found.

## Problem: Binary Search

The recursion starts with left value as '0' and right value as the last index in the input array. For each recursion the middle value of left and right values is calculated, if the element at the middle value index matches the target then the middle index is returned. If the value at middle index is less than target then it must lie in the upper half of the array since the array is sorted, otherwise it must be in the lower half. And so accordingly the left and right values are updated to 'middle-1' or 'middle+1'. In the case of left value becoming larger than the right value -1 is returned because there are no more elements to search in the array and the target has not been found. The recursion will make the left and right value ranges shorter and shorter until the range zeroes in on one element that is equal to the target and it will be returned back up the recursion chain or the range will empty out and the target will not be found and -1 will be returned.

## Identification and Template Introduction

3 parts of a successful binary search:

1. pre-processing: sort the collection if not already sorted.
2. binary search: using a loop or recursion to divide search space into half after each comparision.
3. post-processing: determine valid candidates after the search in the remaining space.

# Template 1

## Binary Search Template I

```
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1
```

Key attributes of template 1:

1. Most basic and elementary form of Binary Search
2. Search condition can be determined without checking the neighbouring elements (or using the specific elements around it).
3. No post-processing required because all elements in the search iteration or recursion are checked and if the target is found it will be returned. Reaching the end of the search means the target was not found.

Distinguishing syntax:

- Initial Condition: left = 0, right = length-1
- Termination: left > right
- Searching Left: right = mid-1
- Searching Right: left = mid+1

## Problem: Sqrt(x)

The left and right values are initialised to 0 and the input 'x'. The middle of the left and right is calculated, if 'x' is between the sqaure values of the middle value and the value just after middle then that means the 'sqaure root of x rounded down to the neatest integet' has been found. Then the middle value will be returned. If instead 'x' is found to be less than the square of middle then that would mean the elements lying to the right of middle cannot have the square root of 'x' and so the right side is eliminated by setting right to 'middle-1'. Otherwise if 'x' is larger than 'middle ^ 2' then that would mean the left side of middle cannot contain the square root of 'x' and so this side is eliminated by setting left to 'middle+1'. The search iteration continues until the answer is found and returned.

## Problem: Guess Number Higher or Lower

The left and right values are set to 0 and 'n' respectively. Search iteration is done until left value passes right value. Middle value of left and right is calculated in each iteration, if the guess function returns 0 for the middle value then that means middle is the right value and it is returned. Otherwise if middle is lower than the guess value (1 is returned by the function) then the right half is searched by setting left to 'middle+1', and if the middle value is higher than the guess value (-1 is returned by the function) then the left half is searched by setting right to 'middle-1'.

## Problem: Search in Rotated Sorted Array

Given the input array is rotated 'k' times to the right the array will contain two increasing slopes in it, where the target lies in the array will be decided by which slope the current middle element is located on. Initially the left and right values are set to 0 and the last index of the input array. Binary search iteration is done until left value crosses right value and middle value is calculated as the average of left and right in each iteration and if it is equal to the target then middle is returned. If the left element of the array is less than equal to the middle element then that means the middle element is located on the left slope of the array. Then if the target is greater than equal to the left element and less than the middle element then it must mean that target is located further down the left slope and the right side of middle is discarded, otherwise the target must lie on the right of middle and the left side is discarded. If the middle element is less than the left element then that means middle is located on the right slope. Then it is checked if the target is less than equal to the right element and less than the middle element. If it is then that means the target is located further up the right slope and the left side of middle is discarded, otherwise the target must lie left of middle and the right side is discarded. If the target is not found and returned in the binary search iteration then -1 is returned since the target was not found.

## Template 2

```
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if nums[left] == target:
        return left
    return -1
```

Key Attributes:

1. An advanced way to implement Binary Search.
2. Use the element's right neighbor to determine if the condition is met and decide whether to go left or right
3. Gurantees that the search space is atleast 2 in size.
4. After the iteration/recursion is done one element will remain unchecked and it will be needed to check that one element and return the correct values accordingly.

Distinguishing Syntax:

- Initial Condition: left = 0, right = length - 1
- Termination: left == right
- Searching Left: right = mid
- Searching Right: left = mid+1

## Problem: First Bad Version

The left and right values are set 0 and 'n' respectively and the search iteration goes until left becomes equal to right. Middle is calculated as the average of left and right and if middle is is not the bad version then that means all values left of middle are also not the bad version and so all the left values are discarded. If middle is the bad version then it is checked if middle is the least bad version. If the value just before the middle is not a bad version then that means the current middle element is the least bad version and the middle value is returned. If the value just before middle is a bad version then that means there possibly is a lesser bad version on the left side of middle and so all the values right of middle are discarded. After the search iteration is done the remaining value is checked to be a bad version and if it is then it is returned.

## Problem: Find Peak Element

The peak element in the input array will be the one whose value is larger than the elements just before and after it. To check this it must be ensured that the element that is being checked is not at either one of the ends of the array which is why the left and right values are set to 1 and 'len(nums)-2' respectively. Before the binary search iteration starts the end cases are checked for the input array being of length 1, the peak element being the starting one, the peak element being the last one, and the corresponding right answers are returned for each. The iteration goes until left crosses right, the middle is calculated as the average of left and right, if the middle element in the array is larger than the elements just before and after it then it is the peak element and middle is returned. If the middle element is not the peak then it can either be located on the left slope or the right slope depending upon whether the middle element is larger than its previous element or not. If middle element is on the left slope then the peak must lie on the right side and so the left side is discarded, for the right slope similar vice versa logic is applied. The iteration will continue until the left-right range zeroes in on the peak element and it is returned.

## Problem: Find Minimum in Rotated Sorted Array

To find the minimum element in a rotated sorted array we need to find the element that is less than its previous one because in a rotated array that element will be the first one in the non rotated version of the same array and it will also be the smallest. The minimum value is set to the first value in the rotated input array, the left value will be 0, and the right will be the last index of the input array. The iteration will go on until left surpasses right and the middle is calculated for each iteration, if the middle element is smaller than its previous element then it is the smallest element in the array and middle is returned. If the middle element is larger than equal to the first element of the array then that means the middle element is on the left slope and the minimum element (the one just after end of the left slope) must lie on the right of the middle and so the left side is discarded, otherwise the middle element is on the right slope and the min element must lie on the left side so the right side of middle is discarded. The iteration will zero in on the min element and return its index eventually.

# Template 3


## Binary Search template 3

```
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1
```

Key Attributes:

1. An alternative way to implement Binary Search
2. Use the element's neighbors to figure out where to go left or right depending upon whether the condition has been met or not.
3. Guarantees search space is atleast 3 in size in each step.
4. After the search recursion/ iteration ends two elements will remain unchecked and they will need to be checked.

Distinguishing syntax:

- Initial Condition: left = 0, right = length-1
- Termination: left + 1 == right
- Searching Left: right = mid
- Searching Right: left = mid

## Problem: Search for a Range

If the length of nums input array is 0 then return `[-1, -1]` because the target cannot be found. The left and right values are assigned to the first and last index of the input array and the answer array is assigned to `[-1, -1]`. Then the first binary search iteration is done to find the leftmost target value. If the element at the middle of left and right is the target and the element before it is not the target then that means the middle element is the leftmost target value in the array and in that case the middle index is stored at the position 0 in the answer array. Otherwise if the middle element is not the leftmost target element then the binary search goes on as usual. After the iteration the left and right values are checked to be equal to target since template 3 is used to implement binary search. The left and right values are initialised to their initial values again and the binary search is again done to find the rightmost target valeu in the input array. If the middle element is found to be the target value and the element right next to it is not the target value then that means middle element is the rightmost element and the middle index is stored in the index '1' of the answer array. Otherwise the binary search continues as usual. After the iteration the left and right values are checked to be equal to the target since the template 3 is used to implement binary search. After both binary search iterations are done the answer array will have the starting and ending indices of the target if the target is found or `[-1, -1]` if the target is not found.

## Problem: Find 'K' closest elements

Binary search is performed and the middle element is calculated and its validity for being the starting element in the returned subarray is checked in each iteration. Left and Right values are assigned to 0 and length of the array minus 'k', this is done because the returned subarray is going to be between 'mid' and 'mid+k' and this length should not go out of bounds. While left is less than right the binary search iteration is done until left becomes equal to right, middle is calculated as the average in each iteration.