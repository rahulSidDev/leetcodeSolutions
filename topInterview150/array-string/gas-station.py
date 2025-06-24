'''
https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        totalSurplus = 0
        surplus = 0
        start = 0

        for i in range(n):
            totalSurplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        
        return -1 if totalSurplus < 0 else start
