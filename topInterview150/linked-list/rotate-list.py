'''
https://leetcode.com/problems/rotate-list/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if the list is empty then return null
        if not head:
            return
        
        # initialise the last node variable and the length variable.
        lastElement = head
        length = 1
        # iterate until the end of the list. after the iteration we will have the entire
        # length of the list and the last node of the list.
        while lastElement.next:
            lastElement = lastElement.next
            length += 1
        
        # update the variable 'k' to its effective value below the length of the list.
        k = k % length
        # connect the last node to the head node making the whole list into a loop.
        lastElement.next = head
        
        # initialise a temp node variable at the start of the list
        tempNode = head
        # iterate and move the temp node until it reaches the last node to be in the 
        # rotated list.
        for _ in range(length-k-1):
            tempNode = tempNode.next
        
        # store the node next to the temp node as it will be the head node of the rotated
        # list and assign null to the next value of temp node which will undo the looping
        # list into a straight list.
        ansNode = tempNode.next
        tempNode.next = None
        
        # return the ans node as it now the head of the rotated list.
        return ansNode
