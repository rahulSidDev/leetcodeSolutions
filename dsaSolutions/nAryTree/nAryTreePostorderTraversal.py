'''
https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/926/
'''
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traversal(node, resArr):
        	# if current node is null then it means a leaf node has been reached and so nothing is returned.
            if not node:
                return
            
            # each child node of the current is traversed first by looping over each and calling the recursing
            # function by passing in the child node.
            for childNode in node.children:
                traversal(childNode, resArr)
            
            # then the current node is appended to the returning array. this will result in all the children
            # nodes being traversed and then the current node being traversed resulting in a postorder traversal.
            resArr.append(node.val)

            # finally the resulting array is returned.
            return resArr
        
        # the first call to the recursion function the root node and the empty array are passed.
        return traversal(root, [])