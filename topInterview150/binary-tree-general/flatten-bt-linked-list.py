'''
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # initialise the current node to root node.
        curr = root

        # iterate until the last node.
        while curr != None:
            # if the left node is not none then execute the following lines.
            if curr.left != None:
                # initialise the rightmost node in the left subtree.
                p = curr.left
                # iterate until 'p' reaches the rightmost node.
                while p.right != None:
                    p = p.right
                
                # move the right subtree to the right of the 'p' node.
                p.right = curr.right
                # move the left subtree of the curr node to the right subtree and set the left subtree
                # to none.
                curr.right = curr.left
                curr.left = None
            
            # move the current node to the right node.
            curr = curr.right
