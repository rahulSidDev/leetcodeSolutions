'''
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # variable to track the root node value from the postorder list in each recursion.
        self.postorderIndx = len(postorder) - 1
        # dict to map indices to node values from the inorder list. it will be used later
        # to get the root node index.
        inorderMap = {val: indx for indx, val in enumerate(inorder)}
        
        def helperRecur(low, high):
            if low > high:
                return None
            
            # in the post order list the root node value will be at the end. this value is
            # taken and the current root node is created.
            currRoot = TreeNode(postorder[self.postorderIndx])
            # the variable is decremented to track the root node value for the next recursion.
            self.postorderIndx -= 1
            
            # take the mid index from the dict. every value left of it in the inorder list will 
            # be in the left subtree and every value right of it will be in the right subtree.
            mid = inorderMap[currRoot.val]
            # recurse on the left subtree by passing mid+1 and high.
            currRoot.right = helperRecur(mid+1, high)
            # do the same for right subtree by passing low and mid-1.
            currRoot.left = helperRecur(low, mid-1)
            return currRoot
        
        # start the recursion with the low and high values as the starting and ending indices
        # from the inorder list.
        return helperRecur(0, self.postorderIndx)
