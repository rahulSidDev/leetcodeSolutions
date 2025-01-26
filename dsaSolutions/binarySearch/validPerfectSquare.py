'''
https://leetcode.com/explore/learn/card/binary-search/137/conclusion/978/
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        
        while left <= right:
            middle = (left + right) // 2
            
            # if middle squared is equal to sum then that means num is a perfect sqaure and it is returned.
            if middle ** 2 == num:
                return True
            # if middle squared is less than num then there must be some no. larger than middle whose square forms
            # num and so the left side is discarded.
            elif middle ** 2 < num:
                left = middle + 1
            # otherwise right side is discarded as the correct value must lie on the left.
            else:
                right = middle - 1
        
        # If the perfect square root values of num were not found in the iteration then the False value is returned
        # since that means that num is not a perfect square.
        return False