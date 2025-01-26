'''
https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1031/
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # minimum element in the rotated array is the starting element in the non rotated array.
        left, right = 0, len(nums)-1
        
        while left < right:
            middle = (left + right) // 2
            
            # if the middle element is larger than the right one then that means middle element in on the left
            # slope and the min element must lie to the right of middle and so the left side is discarded.
            if nums[middle] > nums[right]:
                left = middle + 1
            # otherwise the middle element lies on the right slope and the min element must lie on the left side and
            # so the right side is discarded.
            elif nums[middle] < nums[left]:
                right = middle
            # otherwise middle, left, and right elements are all equal and the right value is decremented by one to
            # either make the middle element hit the min element (if min lies on the left) or make the right element
            # hit the min element (if the min lies on the right).
            else:
                right -= 1
        
        # after the iteration the left element will contain the min element.
        return nums[left]