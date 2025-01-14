'''
https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1374/
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visitedSet = set()
        islandStack = []
        islandCount = 0
        
        def dfsRecurse(grid, indices, visitedSet):
            currNeighs = []
            
            if indices[0] < len(grid)-1:
                currNeighs.append((indices[0]+1, indices[1]))
            if indices[0] > 0:
                currNeighs.append((indices[0]-1, indices[1]))
            if indices[1] < len(grid[0])-1:
                currNeighs.append((indices[0], indices[1]+1))
            if indices[1] > 0:
                currNeighs.append((indices[0], indices[1]-1))
            
            for neigh in currNeighs:
                if neigh not in visitedSet and grid[neigh[0]][neigh[1]] != '0':
                    visitedSet.add(neigh)
                    dfsRecurse(grid, neigh, visitedSet)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visitedSet and grid[i][j] == '1':
                    visitedSet.add((i, j))
                    dfsRecurse(grid, (i, j), visitedSet)
                    islandCount += 1
        
        return islandCount
    
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        visitedSet = set()
        islandQ = []
        islandCount = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visitedSet:
                    islandQ.append((i, j))
                    islandCount += 1

                    while len(islandQ) != 0:
                        currI, currJ = islandQ.pop(0)
                        visitedSet.add((currI, currJ))
                        if currI != 0 and grid[currI-1][currJ] == '1' and (currI-1, currJ) not in visitedSet:
                            islandQ.append((currI-1, currJ))
                            visitedSet.add((currI-1, currJ))
                        if currI != len(grid)-1 and grid[currI+1][currJ] == '1' and (currI+1, currJ) not in visitedSet:
                            islandQ.append((currI+1, currJ))
                            visitedSet.add((currI+1, currJ))
                        if currJ != 0 and grid[currI][currJ-1] == '1' and (currI, currJ-1) not in visitedSet:
                            islandQ.append((currI, currJ-1))
                            visitedSet.add((currI, currJ-1))
                        if currJ != len(grid[0])-1 and grid[currI][currJ+1] == '1' and (currI, currJ+1) not in visitedSet:
                            islandQ.append((currI, currJ+1))
                            visitedSet.add((currI, currJ+1))

        return islandCount