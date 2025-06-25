'''
https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = -1
        left, right = 0, len(height)-1

        while left < right:
            if height[left] < height[right]:
                currHeight = height[left]
            else:
                currHeight = height[right]
            newA = currHeight * (right-left)
            if newA > maxA: maxA = newA
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return maxA
