'''
https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        
        return index
