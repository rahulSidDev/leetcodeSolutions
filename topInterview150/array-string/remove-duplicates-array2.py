'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0

        while p1 < len(nums):
            if nums[p1] != nums[p2]:
                if p1 - p2 > 2:
                    nums[p2+2: ] = nums[p1: ]
                    p2 += 2
                    p1 = p2
                p2 = p1
            
            p1 += 1
        
        if p1 - p2 > 2:
            nums = nums[: p2+2]
        
        return len(nums)
