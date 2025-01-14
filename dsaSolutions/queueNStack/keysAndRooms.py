'''
https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1391/
'''
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visitedRooms = set()
        visitedRooms.add(0)
        keysQ = [key for key in rooms[0]]
        
        while keysQ:
            currKey = keysQ.pop(0)
            if currKey not in visitedRooms:
                visitedRooms.add(currKey)
            
            for nxtKey in rooms[currKey]:
                if nxtKey not in visitedRooms:
                    keysQ.append(nxtKey)

        return len(visitedRooms) == len(rooms)