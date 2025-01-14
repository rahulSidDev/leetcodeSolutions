'''
https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/
'''
class Solution:
    def numSquares(self, n: int) -> int:       
        allSquares = []
        i = 1
        while i * i <= n:
            allSquares.append(i * i)
            i += 1
        
        if allSquares[len(allSquares)-1] == n:
            return 1
        
        squaresSet = set()
        squaresSet.add(n)
        minSquares = 0
        
        while len(squaresSet) != 0:
            minSquares += 1
            tempSet = set()
            
            for currN in squaresSet:                
                for square in allSquares:
                    if currN - square == 0:
                        return minSquares
                    if square > currN:
                        break
                    tempSet.add(currN - square)
            
            squaresSet = tempSet
        
        return 0