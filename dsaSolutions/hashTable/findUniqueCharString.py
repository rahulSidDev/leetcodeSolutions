'''
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1120/
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        
        for key in hashmap:
            if hashmap[key] == 1:
                return s.index(key)
        
        return -1