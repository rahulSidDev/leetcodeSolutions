'''
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1012/
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if the current node is null then return null.
        if not root:
            return None
        
        # if the values of p and q lie on either side of the current node value then the current node itself
        # is the LCA and so it is returned.
        if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root
        
        # if both values of p and q are less than the current node value then the LCA must lie in the 
        # left subtree, and so the function recurses by passing in the left child node.
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # if both values of p and q are greater than the current node value then the LCA must lie in the 
        # right subtree, and so the function recurses by passing in the right child node.
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)