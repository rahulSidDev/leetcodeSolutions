'''
https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        romanToVals = {
            'I': (1,1), 
            'V': (2,5), 
            'X': (3,10), 
            'L': (4,50), 
            'C': (5,100), 
            'D': (6,500), 
            'M': (7,1000)
        }

        count = romanToVals[s[0]][1]
        for i in range(1, len(s)):
            if romanToVals[s[i]][0] > romanToVals[s[i-1]][0]:
                count = count - romanToVals[s[i-1]][1]
                count += romanToVals[s[i]][1] - romanToVals[s[i-1]][1]
            else:
                count += romanToVals[s[i]][1]
        
        return count
