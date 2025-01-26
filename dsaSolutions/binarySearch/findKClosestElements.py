'''
https://leetcode.com/explore/learn/card/binary-search/135/template-iii/945/

find detailed explanation: https://leetcode.com/explore/learn/card/binary-search/135/template-iii/945/discuss/462664/Python-binary-search-with-detailed-explanation
'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # try to find the starting of the k length subarray since the input array is sorted ascending.
        # assign left and right to 0 and len(arr)-k to ensure that k elements in the subarray don't go out of bounds.
        left, right = 0, len(arr) - k
        
        while left < right:
            middle = (left + right) // 2
            
            # if x is less equal to the middle element then that must mean that there is an element left of middle that
            # is less than middle and its absolute difference with x will be lesser. so the right half is discarded.
            if x <= arr[middle]:
                right = middle
            # otherwise if x is greater than equal to the middle+k element from the array then that means there is some element
            # right of the k length subarray whose absolute difference with x is lesser. so the left half is discarded to shift the
            # subarray to the right and include that element.
            elif x >= arr[middle + k]:
                left = middle + 1
            else:
                # if x is between middle and middle+k elements then the middle (start of the k len subarray) is shifted by discarding
                # the right side if x is farther away from the middle+k side or by discarding the left side if its farther from the middle side.
                midDist = abs(x - arr[middle])
                midKDist = abs(x - arr[middle + k])
                if midDist <= midKDist:
                    right = middle
                else:
                    left = middle + 1
        
        # after recursion the left value will be equal to the middle value and equal to the starting of the k len subarray and
        # so the subarray from left to left+k is returned.
        return arr[left: left+k]