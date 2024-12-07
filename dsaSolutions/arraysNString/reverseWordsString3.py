'''
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(x[::-1] for x in s.split())