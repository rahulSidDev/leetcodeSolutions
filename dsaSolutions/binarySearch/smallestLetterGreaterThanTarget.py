'''
https://leetcode.com/explore/learn/card/binary-search/137/conclusion/977/
'''
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # left and right values are set to the first and last indices of the array.
        left, right = 0, len(letters)-1
        # the min value is set to '{' since its ascii value is greater than all the alphabets.
        minGreater = '{'
        
        while left <= right:
            middle = (left + right) // 2
            
            # if the ascii value of middle letter is larger than the target then it is checked if it is smaller
            # than the min value and if it is then it is set as the current min val found that is greter than the target.
            # then the right side is discarded in order to search for an even smaller letter that is greater than the target.
            if ord(letters[middle]) > ord(target):
                if ord(letters[middle]) < ord(minGreater):
                    minGreater = letters[middle]
                right = middle - 1
            
            # otherwise the middle letter is less than equal to the target then the left side is discarded in search for 
            # a letter that is greater than target since the input array of letters is sorted in non-decreasing fashion.
            if ord(letters[middle]) <= ord(target):
                left = middle + 1
        
        # if the min val has the same value as the initial one then that means no letter larger than the target was found
        # and the first letter from the array is returned. otherwise the min val is returned.
        return letters[0] if minGreater == '{' else minGreater