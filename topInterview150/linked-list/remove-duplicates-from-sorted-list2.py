'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node and attach before the list head. this is done to ensure there
        # is a previous node to consider before the head node when the iteration starts.
        dummy = prevNode = ListNode(0)
        dummy.next = head

        # iterate until the current node and the next node are not null.
        while head and head.next:
            if head.val == head.next.val:
                # if the current node and next node are same then iterate until the last node in
                # the current set of duplicate nodes is reached.
                while head and head.next and head.val == head.next.val:
                    head = head.next
                # move the current node to the node just after the set of duplicate nodes.
                head = head.next
                # join the previous node to the current node, effectively removing all the duplicate
                # rows in between.
                prevNode.next = head
            else:
                # if the current node and next node are not same then simply move the previous node
                # and current node to the next.
                prevNode = prevNode.next
                head = head.next
        
        # return the head node which will be the node just after the current node.
        return dummy.next
