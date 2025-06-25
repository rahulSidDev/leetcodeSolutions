'''
https://leetcode.com/problems/path-sum/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helperRecur(root, valSum, targetSum):
            # if the current node is null then the end of the current path has
            # been reached without the target sum being reached and so false is returned.
            if root == None:
                return False
            
            # if the left and right child nodes are none then that means that the last node
            # in the current path has been reached. return true or false based on whether the
            # current sum is equal to the target sum.
            if root.left == None and root.right == None:
                return valSum + root.val == targetSum
            
            # return the ORed value of the results of recursions on the left and right subtrees.
            # if the target sum is reached in any one of the paths then true will be returned to the top.
            return helperRecur(root.left, valSum+root.val, targetSum) or helperRecur(root.right, valSum+root.val, targetSum)
        
        # run the helper function and return the result.
        return helperRecur(root, 0, targetSum)
