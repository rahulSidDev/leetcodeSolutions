'''
https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1105/
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset1 = set()
        hashset2 = set()
        retArr = []
        
        for num in nums1:
            hashset1.add(num)
        
        for num in nums2:
            hashset2.add(num)
        
        intersection = set.intersection(hashset1, hashset2)
        
        for num in intersection:
            retArr.append(num)
        
        return retArr