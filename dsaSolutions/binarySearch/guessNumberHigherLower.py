'''
https://leetcode.com/explore/learn/card/binary-search/125/template-i/951/
'''
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        
        while left <= right:
            middle = (left + right) // 2
            
            if guess(middle) == 0:
                return middle
            elif guess(middle) == 1:
                left = middle + 1
            else:
                right = middle - 1