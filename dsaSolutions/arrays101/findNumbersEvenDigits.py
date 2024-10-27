'''
Given an array 'nums' of integers, return how many of them contain an even number of digits.
'''
class Solution:
    def hasEvenDigits(self, num: int) -> bool:
        digit_count = 0

        while num:
            digit_count += 1
            num //= 10

        return digit_count & 1 == 0 # checking if 'digit_count' is even or not.
    
    def findNumbers(self, nums: List[int]) -> int:
        # Counter to count the number of even digit integers
        even_digit_count = 0

        for num in nums:
            if self.hasEvenDigits(num):
                even_digit_count += 1

        return even_digit_count