'''
Given the 'root' of a binary tree, return the inorder traversal of its nodes' values.
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        returnList = []
        
        def helperRecur(root):
            if root == None:
                return None
            
            helperRecur(root.left)
            returnList.append(root.val)
            helperRecur(root.right)
        
        helperRecur(root)
        return returnList