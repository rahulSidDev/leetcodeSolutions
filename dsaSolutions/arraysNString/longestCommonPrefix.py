'''
https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        shortest = min(strs,key=len)
        
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        
        return shortest