'''
Given an integer array 'nums' sorted in non-decreasing order, return an array of the squares of each number sorted in 
non-decreasing order.
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newNums = []
        for num in nums:
            newNums.append(num*num)
        
        newNums.sort()
        return newNums