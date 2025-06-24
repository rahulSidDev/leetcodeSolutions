'''
https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityNo = len(nums) // 2
        hashMap = {}

        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        
        for key in hashMap:
            if hashMap[key] > majorityNo:
                return key
