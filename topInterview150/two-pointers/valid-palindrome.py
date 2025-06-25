'''
https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        trimmedStr = ''
        for char in s:
            asciiVal = ord(char)
            if asciiVal in range(48,58) or asciiVal in range(97,123):
                trimmedStr += char
        
        left, right = 0, len(trimmedStr)-1
        while left < right:
            if trimmedStr[left] != trimmedStr[right]:
                return False
            left += 1
            right -= 1
        
        return True
