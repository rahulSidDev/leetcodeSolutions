'''
https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/915/
'''
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # if the root node is null then empty list is returned since there is no tree to be traversed.
        if not root:
            return []
        
        # the queue is created with the root node inside of it.
        nodeQ = [root]
        # the empty return array is also created.
        retArr = []
        
        # iteration is done until the entire queue becomes empty.
        while nodeQ:
        	# all the children of all the nodes in the queue are iterated over and the child node values
        	# are added to the currNodeArr array and child nodes themselves are added to the childrenArr
        	# array.
            childrenArr = []
            currNodeArr = []
            for currNode in nodeQ:
                currNodeArr.append(currNode.val)
                childrenArr += currNode.children
            
            # the currNodeArr is added to the return array. the childrenArr array is assigned to the queue
            # since it contains the nodes of the next level in the tree. in this way the queue each time will
            # contain the nodes of the next level and they will be iterated over effectively achieving level order
            # traversal.
            retArr.append(currNodeArr)
            nodeQ = childrenArr
        
        # finally returning array is returned.
        return retArr