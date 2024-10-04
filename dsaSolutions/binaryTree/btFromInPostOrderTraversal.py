'''
Given two integer arrays 'inorder' and 'postorder' where 'inorder' is 
the inorder traversal of a binary tree and 'postorder' is the postorder 
traversal of the same tree, construct and return the binary tree.
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postorderIndx = len(postorder) - 1
        inorderMap = {val: indx for indx, val in enumerate(inorder)}
        
        def helperRecur(low, high):
            if low > high:
                return None
            
            currRoot = TreeNode(postorder[self.postorderIndx])
            self.postorderIndx -= 1
            
            mid = inorderMap[currRoot.val]
            currRoot.right = helperRecur(mid+1, high)
            currRoot.left = helperRecur(low, mid-1)
            return currRoot
        
        return helperRecur(0, self.postorderIndx)