'''
https://leetcode.com/problems/binary-search-tree-iterator/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # variable to store the root of the tree
        self.root = root
        # storing the inorder values of the tree nodes.
        self.inorderArr = []
        # variable to store the pointer of the traversal.
        self.pointer = None

    def next(self) -> int:
        # if the inorder array is empty then traverse the tree and fill up the array by calling 
        # the traverse function.
        if not self.inorderArr:
            self.traverse()
        
        # if the pointer is none then move it to the first index.
        if self.pointer == None:
            self.pointer = 0
        # if the pointer is less than the length of the inorder list then simply increment it by 1.
        elif self.pointer < len(self.inorderArr):
            self.pointer += 1

        # return element pointed to by the pointer.
        return self.inorderArr[self.pointer]

    def hasNext(self) -> bool:
        # if the pointer has reached the end of the inorder array then there are no more elements
        # to the right and so false is returned, otherwise true is returned.
        return self.pointer != len(self.inorderArr)-1
        
    def traverse(self):
        # initialise the root of the binary tree for the helper function
        root = self.root
        
        def helper(node, arr):
            # if the end of the tree is reached then return none.
            if not node:
                return
            
            # perform the inorder traversal by recursing on the left subtree, storing the node value
            # to the array, and then recursing on the right subtree.
            helper(node.left, arr)
            arr.append(node.val)
            helper(node.right, arr)
            
            # return the updated array.
            return arr
        
        # run the helper function and store the returned inorder array to 'inorderArr'.
        self.inorderArr = helper(root, [])

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
