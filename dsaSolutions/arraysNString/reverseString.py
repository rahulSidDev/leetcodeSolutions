'''
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left: int, right: int, string: List[str]):
            if left >= right:
                return
            string[left], string[right] = string[right], string[left]
            return helper(left+1, right-1, string)
        
        helper(0, len(s)-1, s)