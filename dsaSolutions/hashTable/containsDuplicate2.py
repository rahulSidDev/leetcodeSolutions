'''
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1121/
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        
        for i, ele in enumerate(nums):
            if ele not in hashmap:
                hashmap[ele] = i
            else:
                if abs(hashmap[ele] - i) <= k:
                    return True
                else:
                    hashmap[ele] = i
        
        return False