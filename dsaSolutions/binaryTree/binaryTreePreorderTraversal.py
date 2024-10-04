'''
Given the 'root' of a binary tree, return the preorder traversal of its nodes' values.
'''
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        returnList = []
        
        def helperRecur(root):
            if root == None:
                return

            returnList.append(root.val)
            helperRecur(root.left)
            helperRecur(root.right)
        
        helperRecur(root)
        return returnList