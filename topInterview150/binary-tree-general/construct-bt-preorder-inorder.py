'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # variable to store the index of the current root in the preorder list.
        self.preorderIndx = 0
        # dict to map node values to indices from the preorder list to the inorder list.
        inorderMap = {val: indx for indx, val in enumerate(inorder)}
        
        def helperRecur(low, high):
            # return none when low index crosses high index.
            if low > high:
                return None
            
            # the first value in the preorder list will be the root node every recursion.
            # and so the current root node is created using the first value
            currRoot = TreeNode(preorder[self.preorderIndx])
            # increment the variable to track the root node value in the next recursion.
            self.preorderIndx += 1
            
            # get the mid index from the dictionary. every value left of this index will be
            # in the left subtree and every value right of it will be in the right subtree.
            mid = inorderMap[currRoot.val]
            # recurse on the left subtree values by passing low and mid-1.
            currRoot.left = helperRecur(low, mid-1)
            # do the same for right with mid+1 and high.
            currRoot.right = helperRecur(mid+1, high)
            # return the current root
            return currRoot
        
        # start the recursion with the low and high values as the starting and ending indices
        # from the inorder list.
        return helperRecur(0, len(inorder)-1)
