'''
Given an array 'nums' of 'n' integers where 'nums[i]' is in the range '[1, n]', return an array of all the integers in the 
range '[1, n]' that do not appear in 'nums'.
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        
        return res