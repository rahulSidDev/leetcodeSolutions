'''
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/140/introduction-to-a-bst/1008/
'''
class BSTIterator:
	# initialise the root node of the bst, the inorder array to store the node values in inorder fashion,
	# and the pointer to store where the current node value is in the inorder array.
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.inorderArr = []
        self.pointer = None

    def next(self) -> int:
    	# if the inorder array is empty then that means the next function is being called for the first time
    	# after initialisation, and so the traverse function is called to populate the array.
        if not self.inorderArr:
            self.traverse()
        
        # if the pointer is none then that means the next function is being called for the first time after 
        # initialisation and so the pointer is assinged the first index 0.
        if self.pointer == None:
            self.pointer = 0
        # if the pointer is between 0 and the end of the array then just add 1 to it to increase the pointer.
        elif self.pointer < len(self.inorderArr):
            self.pointer += 1

        # return the element from inorder array at the pointer index.
        return self.inorderArr[self.pointer]

    def hasNext(self) -> bool:
        # return whether the pointer is at the end of the inorder array or not.
        return self.pointer != len(self.inorderArr)-1
        
    def traverse(self):
    	# get the root node of the BST.
        root = self.root
        
        def helper(node, arr):
        	# if a null node is reached in the recursion then return null.
            if not node:
                return
            
            # call the function again by passing in the left child to traverse the left sub tree.
            helper(node.left, arr)

            # append the current node to the input array.
            arr.append(node.val)

            # call the function again by passing in the right child to traverse the right sub tree.
            helper(node.right, arr)

            # return the updated array. the order in which the elements are added to the array will be inorder.
            return arr
        
        # call the helper function by passing in the root node.
        self.inorderArr = helper(root, [])