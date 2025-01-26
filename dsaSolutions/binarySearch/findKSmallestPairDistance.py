'''
https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1041/
'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def countPairs(nums, dist):
            # count is the no. of pairs.
            count = 0
            # the left pointer of the sliding window in the array.
            left = 0
            
            for right in range(len(nums)):
                # if the difference of left and right elements is greater than the input distance then
                # move the left pointer forward until the difference becomes less than or equal to the input distance
                while nums[right] - nums[left] > dist:
                    left += 1
                
                # the count of all possible pairs of elements can simply be calculated by adding the differences
                # between left and right indices.
                count += right - left
            
            return count
        
        nums.sort()

        # the search space is the difference between array elements. the smallest possible difference is 0
        # and the largest possible difference is the largest element in the array. These values are assigned
        # to left and right respectively.
        left, right = 0, nums[len(nums)-1]
        while left < right:
            # calculate the difference value between left and right.
            middle = (left + right) // 2
            # count the no. of array element pairs whose difference is less than or equal to 'middle'.
            count = countPairs(nums, middle)
            
            # if the count of pairs is less than 'k' then discard the left side increasing the difference 
            # value so that the no. of valid element pairs is increased to be more than 'k'.
            if count < k:
                left = middle + 1
            # if the count of pairs is greater than or equal to 'k' then discard the right side decreasing
            # the difference value so that the difference between element pairs is minimised.
            else:
                right = middle
        
        # after the iteration the left value will have the 'k-th' smallest distance among all pairs of elements.
        return left