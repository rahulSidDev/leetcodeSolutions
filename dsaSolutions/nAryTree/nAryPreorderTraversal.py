'''
https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/925/
'''
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def traversal(node, resArr):
            # if a leaf node is reached then return nothing.
            if not node:
                return
            
            # the current node value is added to the return array and then each child of the current node
            # is looped over and the recursion function is called by passing in the childnode. this will 
            # result in the current node being visited and then each child element being visited which is
            # the preorder traversal we want.
            resArr.append(node.val)
            for childNode in node.children:
                traversal(childNode, resArr)
            
            # the retarray is returned after the current node has been added and all of its children have 
            # been traversed.
            return resArr
        
        # the first call to the recursion function the root node and the empty array are passed.
        return traversal(root, [])