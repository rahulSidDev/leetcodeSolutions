'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # variable to store the LCA node.
        self.lcaFoundNode = None
        
        def helperRecur(currRoot):
            # if the end of the tree is reached then return none.
            if currRoot == None:
                return False
            
            # recurse on the left and right subtrees.
            foundLeft = helperRecur(currRoot.left)
            foundRight = helperRecur(currRoot.right)
            
            # if the current node val is equal to p or q then return true. if the p or q was 
            # matched while traversing the left or right subtrees then save the current node as the
            # LCA node as well before returning true.
            if currRoot.val == p.val or currRoot.val == q.val:
                if foundLeft == True or foundRight == True:
                    self.lcaFoundNode = currRoot
                return True
            
            # if neither p nor q was found in either of the subtree and neither of them mathced the 
            # node value above then return false.
            if not (foundLeft or foundRight):
                return False
            
            # if p was found in one subtree and q was found in another subtree then save the current 
            # node as the LCA node.
            if foundLeft and foundRight:
                self.lcaFoundNode = currRoot
            
            # return true if none of the conditions above was reached.
            return True  
        
        # run the helper function.
        helperRecur(root)
        # return the LCA found node.
        return self.lcaFoundNode
