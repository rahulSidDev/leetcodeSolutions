'''
https://leetcode.com/explore/learn/card/binary-search/138/background/1038/
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recurse(low, high):
            if low > high:
                return -1
            
            middle = (high - low) // 2
            
            if nums[low+middle] == target:
                return low+middle
            elif nums[low+middle] < target:
                return recurse(low+middle+1, high)
            else:
                return recurse(low, low+middle-1)
        
        return recurse(0, len(nums)-1)