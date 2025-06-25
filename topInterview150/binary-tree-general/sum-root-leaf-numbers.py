'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # variable to store the total sum of the tree.
        self.totalSum = 0

        def helper(node, prevVal):
            # multiply the prev sum with 10 and add the current node value to update the path sum.
            newVal = node.val + prevVal * 10
            
            # if the left child of current node exists then recurse on the left child. same for right child. 
            if node.left: helper(node.left, newVal)
            if node.right: helper(node.right, newVal)

            # if the left and right child both don't exist then this means the current node is a leaf node.
            # in this case add the new sum to the total sum and return back to the parent node.
            if not node.left and not node.right:
                self.totalSum += newVal
                return
        
        # run the helper function which will calculate the sum of all root to leaf path nodes and will
        # store them inside of 'totalSum'
        helper(root, 0)
        # return the totalt sum.
        return self.totalSum
