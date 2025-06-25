'''
https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node with the value of 0 which will serve as the start of the output
        # linked list with the added numbers.
        dummyHead = ListNode(0)
        # initialise tail variable that will keep track of the last node added to the returned 
        # linked list.
        tail = dummyHead
        # carry variable to handle addition results that reach double digits.
        carry = 0
        
        # keep iterating until l1 reaches the end, l2 reached the end and there is no carry
        # left.
        while l1 != None or l2 != None or carry != 0:
            # take the digit1 and digit2 from list1 and list2 for addition.
            digit1 = l1.val if l1 != None else 0
            digit2 = l2.val if l2 != None else 0
            
            # add the two digits and the carry. extract the unit digit and the overflowing
            # digit. update the carry with the overflowing digit.
            summ = digit1 + digit2 + carry
            unitdigit = summ % 10
            carry = summ // 10
            
            # create a new node using the unit digit and add it to the next value of existing
            # tail node.
            tail.next = ListNode(unitdigit)
            # update the tail node to the newly created and added node.
            tail = tail.next
            
            # update l1 and l2 pointers to the next node if they are not none.
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        
        # the addition linked list will start from the node 1 not node 0 and so return the
        # node right after dummy head.
        return dummyHead.next
