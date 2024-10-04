'''
Given the 'root' of a binary tree, check whether it is a mirror of 
itself (i.e., symmetric around its center).
'''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helperRecur(left, right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            
            if left.val == right.val:
                outerpair = helperRecur(left.left, right.right)
                innerpair = helperRecur(left.right, right.left)
                return outerpair and innerpair
            else:
                return False
        
        if root == None:
            return False
        
        return helperRecur(root.left, root.right)