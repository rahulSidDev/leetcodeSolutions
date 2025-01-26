'''
https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1042/
'''
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # the search space will be between the max sum possible with the smallest length subarray (subarray
        # of length 1) and the max sum possible with the largest length subarray (subarray with all elements).
        # minRes and maxRes will contain the lower and higher bounds respectively.
        minRes, maxRes = 0, 0
        for num in nums:
            maxRes += num
            if num > minRes:
                minRes = num
        
        # finalRes will contain the minimized largest sum of the split.
        finalRes = None
        while minRes <= maxRes:
            middle = (minRes + maxRes) // 2
            
            # check if the nums array can be split into 'k' subarrays with each subarray having sum less than
            # equal to middle. if true is returned then finalRes is updated and the higher bound is brought down
            # to minimise the sum of subarrays.
            if self.isPossibility(nums, middle, k):
                finalRes = middle
                maxRes = middle - 1
            # otherwise the lower bound is brought up so that subarrays within 'k' are made possible.
            else:
                minRes = middle + 1
        
        return finalRes
    
    def isPossibility(self, nums, middle, k):
        # stores the no. of sum of current subarray.
        subArrSum = 0
        # stores the no. of subarrays.
        subArrNum = 1
        
        for num in nums:
        	# if adding current num to the subarray sum doesn't make the sum greater than middle then
        	# add the num to the subarray sum.
            if subArrSum + num <= middle:
                subArrSum += num
            # otherwise the subarray sum is reset to the current num and the count of subarrays is incremented
            # since the current subarray stops being valid.
            else:
                subArrNum += 1
                subArrSum = num
        
        # whether the no. of subarrays is less than equal to 'k' or not is returned.
        return subArrNum <= k