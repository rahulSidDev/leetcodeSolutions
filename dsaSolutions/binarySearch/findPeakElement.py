'''
https://leetcode.com/explore/learn/card/binary-search/126/template-ii/948/
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        n = len(nums) - 1
        
        if nums[0] > nums[1]: return 0
        if nums[n] > nums[n-1]: return n
        
        left, right = 1, n-1
        
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] > nums[middle-1] and nums[middle] > nums[middle+1]:
                return middle
            
            if nums[middle] > nums[middle-1]:
                left = middle + 1
            else:
                right = middle - 1
        
        return -1