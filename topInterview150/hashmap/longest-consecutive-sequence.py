'''
https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if the nums list is empty then return 0 as there are no consecutive elements.
        if not nums:
            return 0

        # take the input nums list and make a set out of it.
        numsSet = set(nums)
        # 'maxConsecutive' will store the longest consecutive sequence.
        maxConsecutive = 0

        for x in numsSet:
            # if 'x-1' is not in the nums set then that means the current element 'x' is the
            # start of its consecutive sequence. then the sequence starting with 'x' is iterated
            # and counted.
            if x - 1 not in numsSet:
                # set 'y' as the next value in the sequences starting with 'x'.
                y = x + 1
                # iterate until 'y' is found to be in the nums set and continue to increment 'y'.
                while y in numsSet:
                    y += 1
                
                # find the max between the existing max consecutive sequence length and the lenght of the current
                # sequence. assign this max value to maxConsecutive variable.
                maxConsecutive = max(maxConsecutive, y-x)
        
        # return the max no. of consecutive sequences.
        return maxConsecutive
