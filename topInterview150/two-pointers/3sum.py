'''
https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # array to store result.
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if j > i+1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
        
        return res
