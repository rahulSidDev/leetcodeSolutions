'''
Given an array 'arr' of integers, check if there exist two indices 'i' and 'j' such that :
1. i != j
2. 0 <= i, j < arr.length
3. arr[i] == 2 * arr[j]
'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            product = arr[i] * 2
            lo, hi = 0, len(arr) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] == product and mid != i:
                    return True
                elif arr[mid] < product:
                    lo += 1
                else:
                    hi -= 1
        
        return False