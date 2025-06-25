'''
https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # if the input array is empty then return an empty array.
        if not nums:
            return []
        
        # the array to be returned.
        retArr = []
        # length of the input array.
        numsLen = len(nums)
        # declaring the range variables 'a' and 'b' before the loop to avoid scope errors.
        a = b = None

        for i in range(numsLen):
            # if the index is 0 then simply assign 'a' and 'b' to the first element of the array.
            if i == 0:
                a = b = nums[i]
            # otherwise update 'b' and check if the current element is in the range [a,b] or not.
            else:
                b += 1
                # if the current element is not equal to 'b' then it is out of range and the range
                # string needs to be added to the return array.
                if nums[i] != b:
                    # if 'b-1' is equal to 'a' then that means the range consists of only 1 element.
                    # in which case only add 'a' to the return array.
                    if b - 1 == a:
                        retArr.append(f'{a}')
                    # otherwise the range consists of multiple elements and 'a->b' string is added to the 
                    # return array.
                    else:
                        retArr.append(f'{a}->{b-1}')
                    
                    # update both 'a' and 'b' to be the current element for the next range.
                    a = b = nums[i]
        
        # after the loop if 'a' is less than the last element of the input array then that means the last element
        # is in a range with multiple values and so 'a->b' is added to the ret array.
        if a < nums[numsLen-1]:
            retArr.append(f'{a}->{b}')
        # otherwise the last element is in a range of just one value and 'a' is added to the ret array.
        else:
            retArr.append(f'{a}')
        
        return retArr
