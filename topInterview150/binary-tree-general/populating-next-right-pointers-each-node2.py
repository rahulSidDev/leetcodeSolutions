'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=study-plan-v2&envId=top-interview-150
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # list to store all the nodes in one level.
        level = [root]
        
        # iterate if the root node in not none and until the level list is not empty.
        while root and level:
            # iterate through every node in the level list.
            for i in range(len(level)):
                # if the current node is not the last one in the list then connect its
                # next pointer to the node after it.
                if i != len(level) - 1:
                    level[i].next = level[i+1]
                # otherwise make the next pointer point to none.
                else:
                    level[i].next = None
            
            # initialise the temp list.
            temp = []
            # iterate through every node in level list.
            for node in level:
                # if left child exists for the current node then append it to the temp list.
                if node.left:
                    temp.append(node.left)
                # if right child exists for the current node then append it to the temp list.
                if node.right:
                    temp.append(node.right)
            
            # make the level list the current temp list.
            level = temp
        
        return root
