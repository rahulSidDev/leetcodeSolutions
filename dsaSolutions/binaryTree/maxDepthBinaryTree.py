'''
Given the 'root' of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            
            depthLeft = dfs(root.left, depth)
            depthRight = dfs(root.right, depth)
            return max(depthLeft + 1, depthRight + 1)
        
        return dfs(root, 0)