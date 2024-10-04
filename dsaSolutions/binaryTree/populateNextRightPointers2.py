'''
Given a binary tree:
	struct Node {
	  int val;
	  Node *left;
	  Node *right;
	  Node *next;
	}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should 
be set to 'NULL'. Initially, all next pointers are set to 'NULL'.
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        tempRoot = root
        level = [root]
        
        while tempRoot and level:
            for i in range(len(level)):
                if i != len(level) - 1:
                    level[i].next = level[i+1]
                else:
                    level[i].next = None
            
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level = temp
        
        return root