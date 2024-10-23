'''
Given the 'root' of a binary tree, return the inorder traversal of its nodes' values.
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		# Iterative solution:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right