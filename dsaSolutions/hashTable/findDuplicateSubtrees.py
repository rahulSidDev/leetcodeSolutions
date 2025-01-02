'''
https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1127/
'''
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        pathsHM = {}
        res = []
        
        def recursion(currNode, path):
            if not currNode:
                return '#'

            path += ','.join([str(currNode.val), recursion(currNode.left,path), recursion(currNode.right,path)])
            
            if path not in pathsHM:
                pathsHM[path] = 1
            else:
                pathsHM[path] += 1
                if pathsHM[path] == 2: res.append(currNode)
            
            return path
        
        recursion(root, '')
        #print(pathsHM)
        return res