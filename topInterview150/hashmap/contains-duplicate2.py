'''
https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hashmap to store mapping of elements from nums list to their indices.
        hashmap = {}
        
        for i, ele in enumerate(nums):
            # if the current element is not present inside of hashmap then add it as a key
            # mapping to its index value.
            if ele not in hashmap:
                hashmap[ele] = i
            else:
                # if the current element is present inside of hashmap then that means the same
                # element was present inside the nums list before current element. then the absolute
                # difference between both elements indices is checked and if it is less than 'k' then the 
                # duplicate has been found and true is returned.
                if abs(hashmap[ele] - i) <= k:
                    return True
                # otherwise just add the current element mapped to its index into the hashmap.
                else:
                    hashmap[ele] = i
        
        # if the iteration ends then that means the duplicate was not found because it doesn't 
        # exist and false is returned.
        return False
