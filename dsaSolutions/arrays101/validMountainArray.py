'''
Given an array of integers 'arr', return 'true' if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
1. arr.length >= 3
2. There exists some 'i' with '0 < i < arr.length - 1' such that:
	a. arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
	b. arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
'''
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        l = 0
        r = len(arr) - 1
        
        while l + 1 < len(arr) - 1 and arr[l] < arr[l + 1]: 
            l += 1
        
        while r - 1 > 0 and arr[r] < arr[r - 1]: 
            r -= 1
        
        return l == r