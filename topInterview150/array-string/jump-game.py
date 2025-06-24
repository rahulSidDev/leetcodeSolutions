'''
https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        start = 0
        while start+nums[start] < len(nums)-1:
            possibleJumps = [x for x in range(start+1, start+nums[start]+1)]
            if not possibleJumps:
                return False
            
            maxInd = possibleJumps[0]
            for i in possibleJumps:
                if nums[i] + i > nums[maxInd] + maxInd:
                    maxInd = i
            start = maxInd
        
        return True
