'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. According to the definition 
of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes 'p' and 'q' as the lowest node in 'T' 
that has both 'p' and 'q' as descendants (where we allow a node to be a descendant of itself).”
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lcaFoundNode = None
        
        def helperRecur(currRoot):
            if currRoot == None:
                return False
            
            foundLeft = helperRecur(currRoot.left)
            foundRight = helperRecur(currRoot.right)
            
            if currRoot.val == p.val or currRoot.val == q.val:
                if foundLeft == True or foundRight == True:
                    self.lcaFoundNode = currRoot
                return True
            
            if not (foundLeft or foundRight):
                return False
            
            if foundLeft and foundRight:
                self.lcaFoundNode = currRoot
            
            return True  
        
        helperRecur(root)
        return self.lcaFoundNode