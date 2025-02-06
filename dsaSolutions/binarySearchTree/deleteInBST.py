'''
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1006/
'''
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # if the BST doesn't exist then just return null as there is nothing to delete.
        if not root:
            return root
        
        # if the input key is less than the current root's value then the node to be deleted must lie in
        # the left subtree and so the function calls itself with the left child passed in. the returned subtree
        # root from the recursion is assigned to the current node's left child.
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # otherwise if the input key is larger then the correct node must lie in the right subtree and the
        # function calls itself with the right child passed in. the returned subtree root from the recursion
        # is assigned to the current node's right child.
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # otherwise if the key matches the current node's value then the node to be deleted has been found
        # and the steps to delete the current node are then taken.
        else:
        	# if the current node doesn't have a left child then remove it by returning the right child.
            if not root.left:
                return root.right
            
            # if the current node doesn't have a right child then remove it by returning the right child.
            if not root.right:
                return root.left
            
            # if the current node has both left and right children then find the smallest node value in its
            # right subtree. the found node will be in 'temp'.
            temp = root.right
            while temp.left:
                temp = temp.left
            
            # assign the value of the 'temp' node to the value of the current node and then continue recusion
            # on the right subtree to delete the 'temp' node found earlier.
            root.val = temp.val
            root.right = self.deleteNode(root.right, root.val)
        
        # return the root of the BST with the node with the matching value deleted.
        return root