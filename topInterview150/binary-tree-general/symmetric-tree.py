'''
https://leetcode.com/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helperRecur(left, right):
            # if both input nodes are none then they are the same and true is returned.
            if left == None and right == None:
                return True
            # if either node is none then they are different and false is returned.
            if left == None or right == None:
                return False
            
            # if left value and right value the same then recurse on the inner and outer
            # nodes of the tree and return the logical and value of both recursions.
            if left.val == right.val:
                outerpair = helperRecur(left.left, right.right)
                innerpair = helperRecur(left.right, right.left)
                return outerpair and innerpair
            # otherwise the BT is not symmetric and false is returned.
            else:
                return False
        
        # if the tree is empty return false.
        if root == None:
            return False
        
        # return the true or false returned from the helper function.
        return helperRecur(root.left, root.right)
