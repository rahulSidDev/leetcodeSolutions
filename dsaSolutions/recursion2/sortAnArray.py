'''
Given an array of integers 'nums', sort the array in ascending order and return it. You must solve the problem without 
using any built-in functions in 'O(nlog(n))' time complexity and with the smallest space complexity possible.
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bottom cases: empty or list of a single element.
        if len(nums) <= 1:
            return nums

        pivot = int(len(nums) / 2)
        left_list = self.sortArray(nums[0:pivot])
        right_list = self.sortArray(nums[pivot:])
        return self.merge(left_list, right_list)
    
    def merge(self, left_list, right_list):
        left_cursor = right_cursor = 0
        ret = []
        while left_cursor < len(left_list) and right_cursor < len(right_list):
            if left_list[left_cursor] < right_list[right_cursor]:
                ret.append(left_list[left_cursor])
                left_cursor += 1
            else:
                ret.append(right_list[right_cursor])
                right_cursor += 1

        # append what is remained in either of the lists
        ret.extend(left_list[left_cursor:])
        ret.extend(right_list[right_cursor:])

        return ret