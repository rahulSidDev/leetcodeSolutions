'''
Given the 'root' of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursion(root, minval, maxval):
            if not root:
                return True
            
            if root.val <= minval or root.val >= maxval:
                return False
            
            return recursion(root.left, minval, root.val) and recursion(root.right, root.val, maxval)
        
        return recursion(root, float('-inf'), float('inf'))