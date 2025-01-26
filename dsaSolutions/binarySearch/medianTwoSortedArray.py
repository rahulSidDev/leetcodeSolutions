'''
https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1040/
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # na and nb are the length of nums1 and nums2 arrays.
        na, nb = len(nums1), len(nums2)
        # n is the length of nums1 and nums2 added, it represents the length of sorted(nums1+nums2) array.
        n = na + nb

        def solve(k, aStart, aEnd, bStart, bEnd):
        	# if astart crosses aend then the array nums1 can no longer contain the median so the (k-astart)th
        	# element from nums2 is returned. this is because the value of 'k' is not going to be unchanged after
        	# the entire nums1 array has been put out of consideration.
            if aStart > aEnd:
                return nums2[k-aStart]
            # same for bstart crossing bend.
            if bStart > bEnd:
                return nums1[k-bStart]
            
            # the middle indices of nums1 and nums2 are calculated.
            aIndex, bIndex = (aStart + aEnd) // 2, (bStart + bEnd) // 2
            # the middle elements of nums1 and nums2 are found and stored using the indices above.
            aVal, bVal = nums1[aIndex], nums2[bIndex]

            # if the index of the median of sorted(nums1+nums2) is larger than the sum of middle indices
            # of nums1 and nums2 then either the lower half of nums1 or nums2 is discarded.
            if aIndex + bIndex < k:
            	# if middle element of nums1 is larger than nums2 then the lower half of nums2 is dicarded 
            	# while calling the function again.
                if aVal > bVal:
                    return solve(k, aStart, aEnd, bIndex+1, bEnd)
                # otherwise the lower half of nums1 is discarded as the function calls itself.
                else:
                    return solve(k, aIndex+1, aEnd, bStart, bEnd)
            # otherwise if the median of sorted(nums1+nums2) is less than equal to the sum of middle indices
            # of nums1 and nums2 then either the higher half of nums1 or nums2 is discarded.
            else:
            	# if the middle element of nums1 is larger than nums2 then the higher half of nums1 is discarded
            	# as the function calls itself.
                if aVal > bVal:
                    return solve(k, aStart, aIndex-1, bStart, bEnd)
                # otherwise the higher half of nums2 is discarded as the function calls itself.
                else:
                    return solve(k, aStart, aEnd, bStart, bIndex-1)
        
        # if n is odd then the median element will be the (n/2)th element. this is why the helper function is
        # called only once to get the median of two arrays.
        if n % 2 != 0:
            return solve(n // 2, 0, na-1, 0, nb-1)
        # otherwise if n is even then the median will be the average of (n/2)th element and ((n/2)-1)th element
        # which is why the helper function is called twice to get both results to calculate the median.
        else:
            return (
                solve(n // 2 - 1, 0, na-1, 0, nb-1) +
                solve(n // 2, 0, na-1, 0, nb-1)
            ) / 2