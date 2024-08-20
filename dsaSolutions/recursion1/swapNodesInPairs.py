"""
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        newstart = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(newstart)
        return head