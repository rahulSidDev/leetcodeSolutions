'''
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1117/
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_into_t = {}
        t_into_s = {}
        
        for i in range(len(s)):
            if s[i] in s_into_t and s_into_t[s[i]] != t[i]:
                return False
            
            if t[i] in t_into_s and t_into_s[t[i]] != s[i]:
                return False
            
            s_into_t[s[i]] = t[i]
            t_into_s[t[i]] = s[i]
        
        return True