'''
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1164/
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])