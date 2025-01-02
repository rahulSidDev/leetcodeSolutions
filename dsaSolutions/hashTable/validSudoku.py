'''
https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1126/
'''
class Solution:
    def convertIndexToMS(self, i, j):
        if i < 3 and j < 3:
            return 'ms1'
        elif i < 3 and j < 6:
            return 'ms2'
        elif i < 3 and j < 9:
            return 'ms3'
        elif i < 6 and j < 3:
            return 'ms4'
        elif i < 6 and j < 6:
            return 'ms5'
        elif i < 6 and j < 9:
            return 'ms6'
        elif i < 9 and j < 3:
            return 'ms7'
        elif i < 9 and j < 6:
            return 'ms8'
        elif i < 9 and j < 9:
            return 'ms9'
        else:
            return None
    
    def initialiseHashMap(self, len1, len2):
        sudokuHM = {}
        
        for i in range(len1):
            if 'r'+str(i) not in sudokuHM:
                sudokuHM['r'+str(i)] = []
            
            for j in range(len2):
                if 'c'+str(j) not in sudokuHM:
                    sudokuHM['c'+str(j)] = []
                
                miniSquare = self.convertIndexToMS(i, j)
                
                if miniSquare not in sudokuHM:
                    sudokuHM[miniSquare] = []
        
        return sudokuHM
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudokuHM = self.initialiseHashMap(len(board), len(board[0]))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] not in sudokuHM['r'+str(i)]:
                    sudokuHM['r'+str(i)].append(board[i][j])
                else:
                    print(i,j)
                    return False
                
                if board[i][j] not in sudokuHM['c'+str(j)]:
                    sudokuHM['c'+str(j)].append(board[i][j])
                else:
                    return False
                
                miniSquare = self.convertIndexToMS(i, j)
                
                if board[i][j] not in sudokuHM[miniSquare]:
                    sudokuHM[miniSquare].append(board[i][j])
                else:
                    return False
        
        return True
