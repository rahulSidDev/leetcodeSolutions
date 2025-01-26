'''
https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1029/
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sort both no.s before performing binary search.
        nums1.sort()
        nums2.sort()
        
        # standard binary search helper function with one small change. if the element is found at the middle
        # index then it is deleted from the input array before returning true. this ensures that each element
        # in the result appears as many times as it shows in both the arrays.
        def binarySearch(arr, ele):
            left, right = 0, len(arr)-1
            while left <= right:
                middle = (left+right) // 2
                if arr[middle] == ele:
                    del arr[middle]
                    return True
                elif arr[middle] < ele:
                    left = middle + 1
                else:
                    right = middle - 1
            return False
        
        # iterated over each element of array1 and if it is found (using binary search) in array2 then
        # add it to the result array.
        foundArr = []
        for ele in nums1:
            isFound = binarySearch(nums2, ele)
            if isFound:
                foundArr.append(ele)
        
        # the return array will have all the values that are common between array1 and array2.
        return foundArr