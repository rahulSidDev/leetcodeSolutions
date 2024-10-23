'''
Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku solution must satisfy all of the following rules:
Each of the digits '1-9' must occur exactly once in each row.
Each of the digits '1-9' must occur exactly once in each column.
Each of the digits '1-9' must occur exactly once in each of the 9 '3x3' sub-boxes of the grid.
The '.' character indicates empty cells.
'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isvalid(board, row, col, c):
            for i in range(9):
                if board[i][col] == c:
                    return False
            
            for j in range(9):
                if board[row][j] == c:
                    return False
            
            x0 = (row//3)*3
            y0 = (col//3)*3
            for i in range(3):
                for j in range(3):
                    if board[i+x0][j+y0] == c:
                        return False
            
            return True
        
        def backtrack(board, row, col):
            if row == 9:
                return True
            if col == 9:
                return backtrack(board, row+1, 0)
            if board[row][col] != '.':
                return backtrack(board, row, col+1)
            
            for i in range(1, 10):
                if isvalid(board, row, col, str(i)):
                    board[row][col] = str(i)
                    if backtrack(board, row, col):
                        return True
                    board[row][col] = '.'
            
            return False
        
        backtrack(board, 0, 0)