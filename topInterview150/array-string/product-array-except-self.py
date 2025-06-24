'''
https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardProds = [nums[0]]
        for i in range(1, len(nums)):
            forwardProds.append(nums[i] * forwardProds[i-1])
        
        backwardProds = [nums[len(nums)-1]]
        for i in range(len(nums)-2, -1, -1):
            backwardProds.append(nums[i] * backwardProds[len(nums)-2-i])
        
        returnArr = [1] * len(nums)
        for i in range(len(nums)):
            if i > 0:
                returnArr[i] *= forwardProds[i-1]
            if i < len(nums)-1:
                returnArr[i] *= backwardProds[len(nums)-2-i]
        
        return returnArr
