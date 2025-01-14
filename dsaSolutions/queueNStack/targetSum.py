'''
https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1389/
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        dp = [[0] * (2* totalSum + 1) for _ in range(len(nums))]
        
        # Initialize the first row of the DP table
        dp[0][nums[0] + totalSum] += 1
        dp[0][-nums[0] + totalSum] += 1
        
        # Fill the DP table
        for index in range(1, len(nums)):
            for sumVal in range(-totalSum, totalSum + 1):
                if dp[index - 1][sumVal + totalSum] > 0:
                    dp[index][sumVal + totalSum + nums[index]] += dp[index - 1][sumVal + totalSum]
                    dp[index][sumVal + totalSum - nums[index]] += dp[index - 1][sumVal + totalSum]
        
        # Return the result if the target is within the valid range
        if abs(target) > totalSum:
            return 0
        else:
            return dp[len(nums)-1][target + totalSum]