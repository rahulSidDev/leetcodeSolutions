'''
https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        start = 0
        jumps = 0
        while start+nums[start] < len(nums)-1:
            possibleJumps = [x for x in range(start+1, start+nums[start]+1)]
            maxInd = possibleJumps[0]
            for i in possibleJumps:
                if nums[i] + i > nums[maxInd] + maxInd:
                    maxInd = i
            start = maxInd
            jumps += 1
        
        return jumps+1
