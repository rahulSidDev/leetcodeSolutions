'''
https://leetcode.com/explore/learn/card/binary-search/126/template-ii/949/
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]
        left, right = 0, len(nums)-1
        
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] < nums[middle-1]:
                minVal = nums[middle]
                break
            
            if nums[middle] >= nums[0]:
                left = middle + 1
            else:
                right = middle - 1
        
        return minVal