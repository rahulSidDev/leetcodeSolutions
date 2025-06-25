'''
https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # temporary head for iteration.
        tempHead = head
        # variables to store the node at 'left' position, node at 'right' position, and the node just before the 'left' position.
        leftNode, rightNode, nodeBforeL = None, None, None
        # pointer to track the position of current node.
        i = 1

        # iterate until the current node reaches the end of the list.
        while tempHead:
            # if the current position is just before left then store this node.
            if i == left - 1:
                nodeBforeL = tempHead
            
            # if the current node is at the left position then store it in the 'leftNode'.
            if i == left:
                leftNode = tempHead
            
            # same for the node at right position.
            if i == right:
                rightNode = tempHead
            
            # move the current node to the next one and increment the current position.
            tempHead = tempHead.next
            i += 1

        # initialise the current pointer to point to the node just after the right node.
        currPointer = rightNode.next
        # iterate untile the left node crosses the right node.
        while leftNode != rightNode.next:
            # as the iteration goes on a copy of the current left node is created and it is connected to the 'currPointer'.
            # then the 'currenPointer' is updated to the newly created and connected node. and so the nodes from left to right
            # are reversed by creating copy nodes from left to right and connecting them in chain like fashion to the node right after
            # right node with the left most node connected first.
            newNode = ListNode(leftNode.val, currPointer)
            currPointer = newNode
            leftNode = leftNode.next
        
        # if there are nodes before the left node then connect the node just before the left node to the leftmost node of the newly 
        # reversed part of the list to complete the whole list and return the head.
        if nodeBforeL:
            nodeBforeL.next = currPointer
            return head
        
        # otherwise if there are no nodes before the left node then simply return the current pointer which will hold the leftmost node
        # of the newly reversed part of the list.
        return currPointer
