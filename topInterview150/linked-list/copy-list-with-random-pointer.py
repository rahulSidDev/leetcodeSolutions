'''
https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-interview-150
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if head is none, meaning the list is empty, then return none.
        if not head:
            return
        
        # duplicate nodes.
        curr = head
        while curr:
            # create a new node with the current node's value and its next value pointing
            # to the next node in the original input list.
            newNode = Node(curr.val, curr.next)
            # make the current node's next value point to the newly created node.
            curr.next = newNode
            # move the current node to the next node in the original list by using the 
            # connection the new node has with the next node. after the iteration is complete
            # the original input list will have a duplicate node for each original node and 
            # the duplicate node will be right next to the original.
            curr = newNode.next
        
        # duplicate random connections.
        curr = head
        while curr:
            # if the random value of current node is not null.
            if curr.random:
                # the random connection connects the current node and the random node. to copy
                # this connection the duplicate nodes of current and random need to be connected.
                # this is achieved by assigning the node next to the random node to the random value
                # of the node next to current.
                curr.next.random = curr.random.next
            
            # since the list contains duplicate nodes right next to their original nodes, in order 
            # to jump to the next node a jump of 'next to next' is done.
            curr = curr.next.next
        
        # the new list will contain the duplicated nodes only and so its head will begin from
        # the second node.
        newHead = head.next
        oldHead = head
        # current pointer for new node is created.
        currNew = newHead
        # current pointer for old node is created.
        currOld = oldHead
        while currOld:
            # connect the current old node to the next old node. the next old node can be
            # accessed by jumping two nodes.
            currOld.next = currOld.next.next
            # connect the current new node to the next new node in a similar manner only if
            # the immediate next node is not null.
            currNew.next = currNew.next.next if currNew.next else None
            # since the next old node has been connected to the current old node, the current
            # old node pointer is updated using this connection.
            currOld = currOld.next
            # same with the current new pointer is done.
            currNew = currNew.next
        
        # after the above iteration is done the new and old nodes will be seperated into serperate
        # lists. the head of the new list is returned.
        return newHead
