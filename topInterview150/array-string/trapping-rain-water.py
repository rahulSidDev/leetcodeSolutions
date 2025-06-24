'''
https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # if the no. of bars is 2 or less then collecting water is not possible
        if len(height) <= 2:
            return 0
        
        n = len(height)
        maxLeft, maxRight = height[0], height[n-1] # max left and right start from the first and last elements.
        left, right = 1, n-2 # left and right indices start from the second and second last element.
        waterUnits = 0 # stores the no. of water units.

        while left <= right:
            # if the max element on the left is less than equal to max element on the right
            # then that means the water level will be based on maxLeft. 
            if maxLeft <= maxRight:
                # if left height is larger than max of left then collecting water is not possible
                # and maxLeft is simply updated.
                if height[left] > maxLeft:
                    maxLeft = height[left]
                # otherwise the water will be collectable and the water unit will be added the
                # difference between maxLeft and the left height.
                else:
                    waterUnits += maxLeft - height[left]
                
                # left is incremented by 1
                left += 1
            # otherwise the max height on the right is less than max height on the left then the
            # water level will be based on the maxRight.
            else:
                # similar steps follow
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    waterUnits += maxRight - height[right]
                right -= 1
        
        return waterUnits
