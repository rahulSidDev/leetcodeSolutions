'''
https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # initialise a slow and a fast pointer. the slow one will only jump one node at a
        # time while the fast one will jump two nodes at a time.
        slow_pointer = head
        fast_pointer = head

        # iterate while the fast pointer has a node and a child node.
        while fast_pointer and fast_pointer.next:
            # move slow pointer to the next node.
            slow_pointer = slow_pointer.next
            # move fast pointer to the next to next node.
            fast_pointer = fast_pointer.next.next

            # if the slow and fast pointers meet up on the same node then there exists a cycle
            # in the linked list and true is returned.
            if slow_pointer == fast_pointer:
                return True
        
        # if the iteration is done then that means the fast pointer reached the end of linked list
        # and there was no cycle present and so false is returned.
        return False
