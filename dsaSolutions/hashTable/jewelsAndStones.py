'''
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1136/
'''
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stonesHM = {}
        
        for jewel in jewels:
            stonesHM[jewel] = 0
        
        for stone in stones:
            if stone in stonesHM:
                stonesHM[stone] += 1
        
        stonesCount = 0
        for i in stonesHM:
            stonesCount += stonesHM[i]
        
        return stonesCount