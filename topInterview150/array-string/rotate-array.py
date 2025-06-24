'''
https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
