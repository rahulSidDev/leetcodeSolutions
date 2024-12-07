'''
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1151/
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        
        return index