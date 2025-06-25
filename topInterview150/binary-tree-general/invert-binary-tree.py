'''
https://leetcode.com/problems/invert-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # when the end of the tree is reached then simply return none.
        if root == None:
            return None
        
        # swap the left and right children of current node. this will also cause the left and right
        # subtrees to be swapped as a result.
        temp = root.left
        root.left = root.right
        root.right = temp

        # iterate over the left and right and right subtree respectively.
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return the current node.
        return root
