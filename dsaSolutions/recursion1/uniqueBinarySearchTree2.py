"""
Given an integer 'n', return all the structurally unique BST's 
(binary search trees), which has exactly 'n' nodes of unique values 
from '1' to 'n'. Return the answer in any order.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def allpossiblebst(start, end, memo):
            res = []
            if start > end:
                res.append(None)
                return res
            if (start, end) in memo:
                return memo[(start, end)]
            
            for i in range(start, end+1):
                leftSubTrees = allpossiblebst(start, i - 1, memo)
                rightSubTrees = allpossiblebst(i + 1, end, memo)
                
                for left in leftSubTrees:
                    for right in rightSubTrees:
                        root = TreeNode(i, left, right)
                        res.append(root)
            
            memo[(start, end)] = res
            return res
        
        return allpossiblebst(1, n, memo)