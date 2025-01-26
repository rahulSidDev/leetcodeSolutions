'''
https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1035/
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    	# left and right values are set to the first and last indices of the input array.
        l, r = 0, len(numbers)-1
        
        while l < r:
            s = numbers[l] + numbers[r]

            # if s is equal to target then return the left and right indices with 1 added to each.
            if s == target:
                return [l+1, r+1]
            # if s is less than target then the left indice is incremented by 1 to increase the overall s and
            # bring it closer to target.
            elif s < target:
                l += 1
            # otherwise s is larger than target and to bring s closer to target the right indice is decremented by 1
            # decreasing the sum.
            else:
                r -= 1