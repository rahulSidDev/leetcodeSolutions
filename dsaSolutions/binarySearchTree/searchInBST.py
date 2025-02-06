'''
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1000/
'''
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def rec(root):
        	# if root is not null then continue the recursive traversal.
            if root:
            	# if the value of current node matches the input value then the desired node has been found
            	# and so the current node is returned.
                if root.val == val:
                    return root
                # if current node's value is less than input value then the correct node must lie in the right
                # subtree and so the recursive function is called by passing in the right child of current node.
                elif root.val < val:
                    return rec(root.right)
                # otherwise the correct node must lie in the left subtree and the function is called by passing
                # in the left node child.
                else:
                    return rec(root.left)
        
        # return the found node with the input value in the BST or return null if the value is not found.
        return rec(root)