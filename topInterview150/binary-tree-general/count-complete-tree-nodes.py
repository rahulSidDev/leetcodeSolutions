'''
https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # if the current root node is none then return 0.
        if not root:
            return 0
        
        # call the get depth function to get the heights of both left and right subtrees.
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)

        # if the left and right subtree have the same height then calculate the no. of nodes in the left
        # subtree plus the current node, and recurse on the right subtree to get to the rightmost node in the last level.
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        # otherwise calculate the nodes in the right subtree plus the current node, and recurse over the left
        # subtree to get to the rightmost node in the last level.
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)
    
    def getDepth(self, node):
        # if the end of the tree is reached then return 0.
        if not node:
            return 0
        
        # recurse over the leftmost path to get the max depth of the current subtree.
        return 1 + self.getDepth(node.left)
