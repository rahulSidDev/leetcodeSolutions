'''
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/143/appendix-height-balanced-bst/1027/
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(node):
        	# if current node is null then return 0 as the end of the tree has been reached and the height
        	# of the tree from the end is 0.
            if not node:
                return 0
            
            # recursively traverse left nodes then the right nodes, effectively making a postorder traversal.
            left = recurse(node.left)
            right = recurse(node.right)
            
            # if the left subtree is unbalanced or the right subtree is unbalanced or the absolute diff between
            # left and right subtree heights is greater than 1 then the whole tree is unbalaned and so -1 is returned
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            
            # otherwise the tree is balanced uptil the current recursion and the max height of left and right
            # subtrees plus 1 is returned.
            return max(left, right) + 1
        
        # a bottom up recursion function is implemented that returns the max height of the tree if it is
        # balanced or it returns -1 if the tree is not balanced. the function returns true/false depending
        # upon whether the recusion function returns -1 or not.
        return recurse(root) != -1