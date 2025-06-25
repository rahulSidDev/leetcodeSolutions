'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # variable to store the sum of the max sum path.
        self.maxSum = float('-inf')

        def dfs(node):
            # if the end of the node is reached then return 0.
            if not node:
                return 0
            
            # recurse on the left subtree and only the positive values from the recursion are considered.
            leftSum = max(0, dfs(node.left))
            # same for the right subtree.
            rightSum = max(0, dfs(node.right))

            # if the cumulative sum of left subtree and right subtree and the current node is larger than
            # the max sum then the max sum is updated with its value. this is to account for the path that
            # goes from the left subtree to the right subtree connected by the current node.
            self.maxSum = max(self.maxSum, leftSum + rightSum + node.val)

            # return the largest of the left and right subtree sum plus the current node value.
            return max(leftSum, rightSum) + node.val
        
        # run the dfs function.
        dfs(root)
        # return the max sum.
        return self.maxSum
