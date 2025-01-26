'''
https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            middle = (right + left) // 2
            
            if middle * middle <= x < (middle+1) * (middle+1):
                return middle
            elif x < middle * middle:
                right = middle - 1
            else:
                left = middle + 1