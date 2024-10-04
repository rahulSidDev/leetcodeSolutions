'''
Given two integer arrays 'preorder' and 'inorder' where 'preorder' is the preorder traversal of a binary tree and 
'inorder' is the inorder traversal of the same tree, construct and return the binary tree.
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorderIndx = 0
        inorderMap = {val: indx for indx, val in enumerate(inorder)}
        
        def helperRecur(low, high):
            if low > high:
                return None
            
            currRoot = TreeNode(preorder[self.preorderIndx])
            self.preorderIndx += 1
            
            mid = inorderMap[currRoot.val]
            currRoot.left = helperRecur(low, mid-1)
            currRoot.right = helperRecur(mid+1, high)
            return currRoot
        
        return helperRecur(0, len(inorder)-1)