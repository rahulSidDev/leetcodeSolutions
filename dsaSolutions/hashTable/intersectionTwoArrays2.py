'''
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1178/
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset = {}
        
        for num in nums1:
            if num not in hashset:
                hashset[num] = 1
            else:
                hashset[num] += 1
        
        retArr = []
        
        for num in nums2:
            if num in hashset:
                retArr.append(num)
                hashset[num] -= 1
                if hashset[num] == 0: del hashset[num]
        
        return retArr