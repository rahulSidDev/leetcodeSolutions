'''
https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWord = ''
        reachedWord = False
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ' and reachedWord:
                break
            if s[i] != ' ':
                reachedWord = True
                lastWord += s[i]
        
        return len(lastWord)
