'''
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1361/
'''
class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            '(': ')', '{': '}', '[': ']'
        }
        bracketStack = []
        
        for char in s:
            if char in bracketMap:
                bracketStack.append(char)
            else:
                if len(bracketStack) == 0:
                    return False
                lastBrac = bracketStack.pop()
                if bracketMap[lastBrac] != char:
                    return False
        
        return len(bracketStack) == 0