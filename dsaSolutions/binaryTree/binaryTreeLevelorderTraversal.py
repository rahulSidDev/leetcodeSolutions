'''
Given the 'root' of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, level = [], [root]
        
        while root and level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level = temp
        
        return ans