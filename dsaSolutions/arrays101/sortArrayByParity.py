'''
Given an integer array 'nums', move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] % 2 == 0:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        
        return nums