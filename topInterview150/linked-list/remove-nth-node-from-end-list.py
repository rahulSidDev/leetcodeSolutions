'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initialise the fast and slow pointer with the head pointer values.
        fast, slow = head, head
        
        # move the fast pointer ahead in the linked list n number of times. doing this will
        # result in fast and slow pointers being exactly n nodes apart.
        for _ in range(n):
            fast = fast.next
        
        # if fast pointer is none then it has reached the end of the list
        # and the nth node to be removed from the end of the list is the head.
        if fast == None:
            return head.next
        
        # move both the fast and slow pointers to their next node until the fast pointer reaches
        # the last node of the linked list.
        while fast.next:
            fast, slow = fast.next, slow.next
        
        # with there being a difference of n nodes between slow and fast pointers and the fast pointer
        # being at the last node, the slow pointer will point to the node just before the nth node from
        # the list's end. and so the slow node's next value is assigned to the next to next node effectively
        # deleting the nth last node.
        slow.next = slow.next.next
        
        return head
