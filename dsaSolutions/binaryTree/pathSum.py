'''
Given the 'root' of a binary tree and an integer 'targetSum', return 'true' 
if the tree has a root-to-leaf path such that adding up all the values 
along the path equals 'targetSum'. A leaf is a node with no children.
'''
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helperRecur(root, valSum, targetSum):
            if root == None:
                return False
            
            if root.left == None and root.right == None:
                return valSum + root.val == targetSum
            
            return helperRecur(root.left, valSum+root.val, targetSum) or helperRecur(root.right, valSum+root.val, targetSum)
        
        return helperRecur(root, 0, targetSum)