"""
Write a function that reverses a string. The input string is given as an array of characters 's'.
You must do this by modifying the input array 'in-place' with 'O(1)' extra memory.
"""
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