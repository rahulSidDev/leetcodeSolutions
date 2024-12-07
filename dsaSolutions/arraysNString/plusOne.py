'''
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        
        for i in range(len(digits)):
            number += digits[i] * pow(10, len(digits)-i-1)
        
        return [int(i) for i in str(number+1)]