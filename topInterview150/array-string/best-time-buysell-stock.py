'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        profit = 0
        currentMax = 0
        for i in range(1, len(prices)):
            currentMax += prices[i] - prices[i-1]
            currentMax = max(0, currentMax)
            profit = max(profit, currentMax)
        
        return profit
