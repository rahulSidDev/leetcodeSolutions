'''
https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        ind = 0
        for char in t:
            if char == s[ind]:
                ind += 1
                if ind == len(s):
                    return True
        
        return False
