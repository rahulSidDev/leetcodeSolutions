'''
https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1039/
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # left and right are the range in which each element from the input array can lie.
        left, right = 0, len(nums)-1
        
        while left < right:
            middle = (left + right) // 2

            # count the the no. of elements in the input array that are less than equal to the middle value.
            count = 0
            for num in nums:
                if num <= middle:
                    count += 1
            
            # ideally the count of elements less than equal to middle value should be equal to the middle value,
            # and if the count is greater than middle then that means there is a value less than or equal to middle 
            # that is repeating in the input array, and so the right side is discarded in search for the repeating value.
            if count > middle:
                right = middle
            # otherwise none of the values less than or equal to middle are repeating in the input array and the repeating
            # value must lie on the right side so the left side is discarded.
            else:
                left = middle + 1
        
        # the iteration zeroes in on the repeating value in the input array and after the iteration is done the left
        # value will be the repeating value.
        return left