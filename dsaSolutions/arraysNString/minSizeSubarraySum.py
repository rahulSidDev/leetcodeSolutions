'''
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        currSum = 0
        minLength = len(nums) + 1
        
        while right < len(nums):
            currSum += nums[right]
            
            while currSum >= target:
                minLength = min(minLength, right-left+1)
                currSum -= nums[left]
                left += 1
            
            right += 1
        
        return minLength if minLength <= len(nums) else 0