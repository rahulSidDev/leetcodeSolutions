'''
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
'''
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i+j not in d:
                    d[i+j] = [mat[i][j]]
                else:
                    d[i+j].append(mat[i][j])
        
        ans = []
        for entry in d.items():
            if entry[0] % 2 == 0:
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        
        return ans