'''
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1301/
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maxCount = 0    
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxCount = max(count, maxCount)
                count = 0
                
        return max(count, maxCount)