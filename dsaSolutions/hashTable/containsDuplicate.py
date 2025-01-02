'''
https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for num in nums:
            if num in hashset:
                return True
            
            hashset.add(num)
        
        return False