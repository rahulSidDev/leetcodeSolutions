'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            # if the end of the BT is reached then return the current depth value.
            if not root:
                return depth
            
            # recurse on the left subtree and store its max depth.
            depthLeft = dfs(root.left, depth)
            # do the same on the right subtree.
            depthRight = dfs(root.right, depth)

            # add 1 to the max depths from both subtrees to account for the current node
            # and then return the max of the two values.
            return max(depthLeft + 1, depthRight + 1)
        
        # run the recursive function. the result returned will be the max depth.
        return dfs(root, 0)
