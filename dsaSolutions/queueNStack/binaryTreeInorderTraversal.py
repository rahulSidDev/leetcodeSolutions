'''
https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1383/
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''Recursive solution:
        returnList = []
        
        def helperRecur(root):
            if root == None:
                return None
            
            helperRecur(root.left)
            returnList.append(root.val)
            helperRecur(root.right)
        
        helperRecur(root)
        return returnList'''
        
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

        return res