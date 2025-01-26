'''
https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left, right, ans = 0, len(nums)-1, [-1, -1]
        while left + 1 < right:
            middle = (left + right) // 2
            
            if nums[middle] == target and nums[middle-1] != target:
                ans[0] = middle
            
            if nums[middle] >= target:
                right = middle
            else:
                left = middle

        if nums[left] == target:
            ans[0] = left
        elif nums[right] == target:
            ans[0] = right

        left, right = 0, len(nums)-1
        while left + 1 < right:
            middle = (left + right) // 2
            
            if nums[middle] == target and nums[middle+1] != target:
                ans[1] = middle
            
            if nums[middle] <= target:
                left = middle
            else:
                right = middle

        if nums[right] == target:
            ans[1] = right
        elif nums[left] == target:
            ans[1] = left
        
        return ans