'''
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])