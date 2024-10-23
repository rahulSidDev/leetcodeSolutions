'''
Write an efficient algorithm that searches for a value 'target' in an 'm x n' integer matrix 'matrix'. This matrix has the following 
properties:
1. Integers in each row are sorted in ascending from left to right.
2. Integers in each column are sorted in ascending from top to bottom.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None:
            return False
        
        row = 0
        col = len(matrix[0]) - 1
        while col >= 0 and row <= len(matrix)-1:
            if target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
            else:
                return True
        
        return False