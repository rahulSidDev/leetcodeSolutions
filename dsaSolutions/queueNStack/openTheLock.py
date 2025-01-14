'''
https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1375/
'''
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        lockMappings = {
            'forward': {
                '0':'1','1':'2','2':'3','3':'4','4':'5','5':'6','6':'7','7':'8','8':'9','9':'0'
            },
            'backward': {
                '0':'9','1':'0','2':'1','3':'2','4':'3','5':'4','6':'5','7':'6','8':'7','9':'8'
            }
        }
        combinationsQ = []
        visitedSet = set(deadends)
        turns = 0
        
        if '0000' in visitedSet:
            return -1
        
        combinationsQ.append('0000')
        visitedSet.add('0000')
        
        while len(combinationsQ) != 0:
            currPossibleCombs = len(combinationsQ)
            
            for _ in range(currPossibleCombs):
                currComb = combinationsQ.pop(0)
                if currComb == target:
                    return turns

                for i in range(4):
                    newForwardComb = list(currComb)
                    newForwardComb[i] = lockMappings['forward'][newForwardComb[i]]
                    newForwardComb = ''.join(newForwardComb)

                    if newForwardComb not in visitedSet:
                        combinationsQ.append(newForwardComb)
                        visitedSet.add(newForwardComb)

                    newBackwardComb = list(currComb)
                    newBackwardComb[i] = lockMappings['backward'][newBackwardComb[i]]
                    newBackwardComb = ''.join(newBackwardComb)

                    if newBackwardComb not in visitedSet:
                        combinationsQ.append(newBackwardComb)
                        visitedSet.add(newBackwardComb)
            
            turns += 1
        
        return -1