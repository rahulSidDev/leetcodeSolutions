'''
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum, rightsum = 0, sum(nums)
        
        for i, ele in enumerate(nums):
            rightsum -= ele
            if rightsum == leftsum:
                return i
            leftsum += ele
        
        return -1