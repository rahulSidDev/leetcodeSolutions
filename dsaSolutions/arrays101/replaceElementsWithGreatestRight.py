'''
Given an array 'arr', replace every element in that array with the greatest element among the elements to its right, and replace 
the last element with '-1'.
After doing so, return the array.
'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1
        i = len(arr) - 1
        
        while i >= 0:
            temp = arr[i]
            arr[i] = m
            if temp > m:
                m = temp
            i-= 1
        
        return arr