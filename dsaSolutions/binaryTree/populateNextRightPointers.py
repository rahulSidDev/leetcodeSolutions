'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
The binary tree has the following definition:
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        tempRoot = root
        level = [tempRoot]
        
        while tempRoot and level:
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
            level = temp
            
            for node in range(len(level)-1):
                level[node].next = level[node+1]
        
        return root