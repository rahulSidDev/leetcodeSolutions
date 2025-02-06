'''
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/140/introduction-to-a-bst/997/
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursion(root, minval, maxval):
            # if the current node is null then return true as a leaf node has been reached.
            if not root:
                return True
            
            # if the current node has value greater than or equal to the max val or less than equal to the min val
            # then that makes the tree an invalid binary search tree and so false is returned.
            if root.val <= minval or root.val >= maxval:
                return False
            
            # the recusion function is called twice with root.left and root.right passed in and the and result returned
            # is the 'anded' value of both. if any of the left or right subtrees are found to be not valid then the whole
            # tree will be not valid.
            return recursion(root.left, minval, root.val) and recursion(root.right, root.val, maxval)
        
        # the first call to recursion function will pass the root node, -infinity float value for minimum val, and
        # infinity float value for maximum val. this is because the root node doesn't have any parents and so it can
        # have any value as valid.
        return recursion(root, float('-inf'), float('inf'))