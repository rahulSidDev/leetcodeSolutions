'''
https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1): # the +1 ensures that the last char in 'haystack' is not missed
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1