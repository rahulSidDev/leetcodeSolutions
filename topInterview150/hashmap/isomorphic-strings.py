'''
https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # hashmap to store 's' characters' mappings to 't' characters.
        s_into_t = {}
        # hashmap to store 't' characters' mappings to 's' characters.
        t_into_s = {}
        
        # iterate over each character of 's' and 't' simultaneously since both have the 
        # same length.
        for i in range(len(s)):
            # if current char from 's' is in the first hashmap and it's not mapped to the
            # current char from 't' then that means the current char has multiple mappings.
            # and so 's' and 't' are not isomorphic, which is why false is returned.
            if s[i] in s_into_t and s_into_t[s[i]] != t[i]:
                return False
            
            # same logic as above except 's' and 't' are swapped and the second hashmap is used.
            if t[i] in t_into_s and t_into_s[t[i]] != s[i]:
                return False
            
            # map the current char from 's' to char from 't' in the first hashmap.
            s_into_t[s[i]] = t[i]
            # do the vice versa for the second hashmap.
            t_into_s[t[i]] = s[i]
        
        # if no incorrect mappings are found then 's' and 't' are isomorphic and return True.
        return True
