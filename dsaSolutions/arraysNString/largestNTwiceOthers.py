'''
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
'''
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        ind = nums.index(largest)
        
        for i in nums:
            if i * 2 > largest and i != largest:
                return -1
        
        return ind