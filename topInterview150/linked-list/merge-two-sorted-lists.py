'''
https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if either list1 or list2 is empty then return the other list that is not empty.
        if not list1 or not list2:
            return list1 or list2

        # if the value of list1 node is less than equal to list2 then move the list1 pointer
        # ahead in the first list.
        if list1.val <= list2.val:
            # when either list pointer reaches the end and recurses back the node with the value
            # just larger than the current one will be returned and the current node will connect
            # to it, chaining the two lists across to create one single sorted list.
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        # otherwise list2 pointer will be moved forward in the second list.
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
