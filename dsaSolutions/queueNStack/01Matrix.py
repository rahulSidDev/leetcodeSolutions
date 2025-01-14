'''
https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1388/
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visitedSet = set()
        queue = []
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visitedSet.add((i, j))
                    queue.append((i, j))
        
        while queue:
            x, y = queue.pop(0)
            
            for offset in [(1,0), (-1,0), (0,1), (0,-1)]:
                newX, newY = x+offset[0], y+offset[1]
                if newX >= 0 and newX <= len(mat)-1 and newY >= 0 and newY <= len(mat[0])-1 and (newX, newY) not in visitedSet:
                    mat[newX][newY] = mat[x][y] + 1
                    queue.append((newX, newY))
                    visitedSet.add((newX, newY))
        
        return mat