'''
https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to store nums elements mapping to their respective indices.
        numsToInd = {}
        
        for ind, ele in enumerate(nums):
            # for each element in nums its pair value can be calculated by finding the 
            # difference between 'target' and the current element.
            possibleVal = target - ele

            # if the pair value of current element is found in the hashmap then that means
            # the pair value exists in the nums list before the current ele. and so the
            # current element and pair element make up the target together and the array containing
            # the indices of both is returned.
            if possibleVal in numsToInd:
                return [numsToInd[possibleVal], ind]
            
            # add the current ele to the hashmap mapping it to the curr ele's index.
            numsToInd[ele] = ind
        
        # if the iteration completes then that means the pair was not found and so an empty
        # list is returned.
        return []
