'''
https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1034/
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sort both arrays to perform binary search.
        nums1.sort()
        nums2.sort()
        
        # basic binary search helper function to find 'ele' element in the array 'arr'.
        def binarySearch(arr, ele):
            left, right = 0, len(arr)-1
            while left <= right:
                middle = (left+right) // 2
                if arr[middle] == ele:
                    return True
                elif arr[middle] < ele:
                    left = middle + 1
                else:
                    right = middle - 1
            return False
        
        # create a set to store elements from the first array that are found in the second array.
        foundSet = set()
        for num1 in nums1:
        	# if the current element has not been found in the second array (not in set) then search it in
        	# the second array using binary search. if it is found then add it to the set.
            if num1 not in foundSet:
                isFound = binarySearch(nums2, num1)
                if isFound:
                    foundSet.add(num1)
        
        # put all found elements from the set into an array and return that array.
        returnArr = []
        for i in foundSet:
            returnArr.append(i)
        
        return returnArr