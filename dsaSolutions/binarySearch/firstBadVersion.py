'''
https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/
'''
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            middle = (left + right) // 2
            
            if isBadVersion(middle) == False:
                left = middle + 1
            else:
                if isBadVersion(middle-1) == False:
                    return middle
                else:
                    right = middle - 1

        if isBadVersion(left):
            return left