'''
https://leetcode.com/explore/learn/card/n-ary-tree/131/recursion/919/
'''
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def traverse(node, currCount, maxCount):
            # if the current node is null then 0 is returned since a leaf node of the tree has been reached.
            if not node:
                return 0
            
            # each child node of the current node is iterated over and the traverse function is called by 
            # passing in the child node and the current count incremented by 1 and the maxcount. the result
            # returned is assigned to the maxcount.
            for childNode in node.children:
                maxCount = traverse(childNode, currCount+1, maxCount)
            
            # if the height of the current node is more than the maxcount then the maxcount is updated.
            maxCount = max(currCount, maxCount)
            # max count is returned.
            return maxCount
        
        # the traverse function is first called by passing in the root node, 1, and -infinity float value.
        return traverse(root, 1, float('-inf'))