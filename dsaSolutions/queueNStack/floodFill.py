'''
https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1393/
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = [(sr, sc)]
        visitedSet = set()
        originalVal = image[sr][sc]
        
        while queue:
            currI, currJ = queue.pop(0)
            image[currI][currJ] = color
            visitedSet.add((currI, currJ))
            
            if currI != 0 and image[currI-1][currJ] == originalVal and (currI-1, currJ) not in visitedSet:
                queue.append((currI-1, currJ))
            if currI != len(image)-1 and image[currI+1][currJ] == originalVal and (currI+1, currJ) not in visitedSet:
                queue.append((currI+1, currJ))
            if currJ != 0 and image[currI][currJ-1] == originalVal and (currI, currJ-1) not in visitedSet:
                queue.append((currI, currJ-1))
            if currJ != len(image[0])-1 and image[currI][currJ+1] == originalVal and (currI, currJ+1) not in visitedSet:
                queue.append((currI, currJ+1))
        
        return image