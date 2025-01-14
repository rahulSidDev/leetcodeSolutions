'''
https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1392/
'''
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        visitedSet = set()
        sameNodeMap = {}
        nodeStack = [node]
        
        while nodeStack:
            currNode = nodeStack.pop()
            
            if currNode in visitedSet:
                continue
            
            visitedSet.add(currNode)
            if currNode not in sameNodeMap:
                sameNodeMap[currNode] = Node(currNode.val)
            
            for neigh in currNode.neighbors:
                if neigh not in sameNodeMap:
                    sameNodeMap[neigh] = Node(neigh.val)
                
                sameNodeMap[currNode].neighbors.append(sameNodeMap[neigh])
                nodeStack.append(neigh)
        
        return sameNodeMap[node]