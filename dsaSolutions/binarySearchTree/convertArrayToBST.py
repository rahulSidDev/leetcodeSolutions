'''
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/143/appendix-height-balanced-bst/1015/
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recurse(start, end):
        	# if the start passes the end value then return null as the search space has been exhausted.
            if start > end:
                return None
            
            # calculate the middle value of start and end indices.
            mid = (start + end) // 2
            
            # create a tree node of the middle value. then recurse on the left side
            # of the middle value by passing the left side in the recursion call, then
            # assign the result to the left child of current node. then do the same wth
            # the right side and the right child.
            node = TreeNode(nums[mid])
            node.left = recurse(start, mid-1)
            node.right = recurse(mid+1, end)
            
            # return the node after inorder traversal of child nodes is done.
            return node
        
        # make the first call to the recursion by passing in 0 and the last index of the input array.
        # the recursive function will perform binary search traversal and create a node of the middle
        # element and assign the traversal result of the lower half to the left child and the traversal
        # result of the right half to the right child. this will result in the array being converted to BST.
        return recurse(0, len(nums)-1)