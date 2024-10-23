class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, columns, diag, antidiag):
            n = len(columns)
            count = 0
            if row == n:
                return 1
            
            for col in range(n):
                if not columns[col] and not diag[row+col] and not antidiag[row-col+n-1]:
                    columns[col] = diag[row+col] = antidiag[row-col+n-1] = True
                    count += backtrack(row+1, columns, diag, antidiag)
                    columns[col] = diag[row+col] = antidiag[row-col+n-1] = False
            
            return count
        
        columns = [False] * n
        diag = [False] * (2*n-1)
        antidiag = [False] * (2*n-1)
        
        return backtrack(0, columns, diag, antidiag)