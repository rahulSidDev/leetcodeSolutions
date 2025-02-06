'''
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1003/
'''
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        
        # if there is no BST then just return the new node as after inserting it, it will be the only node
        # in the BST.
        if not root:
            return newNode
        
        def traverse(node, val):
        	# if node is null then return null.
            if not node:
                return None
            
            # if current node's value is greater than the input value then the correct node must lie in the 
            # left subtree and so the recursion is continued by passing in the left child.
            if node.val > val:
                retval = traverse(node.left, val)
            # otherwise the correct node must lie in the right subtree and so the recursion is continued by
            # passing in the right child.
            else:
                retval = traverse(node.right, val)

            # if the value returned is null then that means that the current node is the leaf node where
            # the new node will be inserted and so it is set as the return value.
            if retval == None:
                retval = node
            
            # the correct return value is returned and it returns all the way to the top of the recursion
            # stack to give the correct node to insert at.
            return retval
        
        # traverse the BST to find the correct node to insert the new node at.
        foundNode = traverse(root, val)
        
        # if the new val is greater than the foundNode's value then insert the new node as the right child
        # of the foundNode.
        if val > foundNode.val:
            foundNode.right = newNode
        # otherwise insert it as the left child of foundNode.
        else:
            foundNode.left = newNode
        
        # return the root of the BST with the inserted new node.
        return root