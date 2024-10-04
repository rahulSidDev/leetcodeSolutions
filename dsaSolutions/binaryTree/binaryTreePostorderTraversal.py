'''
Given the 'root' of a binary tree, return the postorder traversal of its nodes' values.
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        returnList = []
        
        def helperRecur(root):
            if root == None:
                return None
            
            helperRecur(root.left)
            helperRecur(root.right)
            returnList.append(root.val)
        
        helperRecur(root)
        return returnList