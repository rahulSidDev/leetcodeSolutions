'''
Given an array 'nums' of distinct integers, return all the possible permutations. You can return the answer in any order.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recur(nums, path, res):
            if not nums:
                res.append(path)
            
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                newPath = path + [nums[i]]
                recur(newNums, newPath, res)
            
            return res
        
        return recur(nums, [], [])