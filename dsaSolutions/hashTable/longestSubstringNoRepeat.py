'''
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1135/
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        maxCount = 0
        
        for i in range(len(s)):
            countSet = set()
            for j in range(i, len(s)):
                if s[j] not in countSet:
                    countSet.add(s[j])
                    maxCount = max(maxCount, (j - i + 1))
                else:
                    break
        
        return maxCount