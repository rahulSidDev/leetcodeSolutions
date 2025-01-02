'''
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1115/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsToInd = {}
        
        for ind, ele in enumerate(nums):
            possibleVal = target - ele
            if possibleVal in numsToInd:
                return [numsToInd[possibleVal], ind]
            
            numsToInd[ele] = ind
        
        return []