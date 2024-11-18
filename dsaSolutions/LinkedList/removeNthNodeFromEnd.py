'''
https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        
        for _ in range(n):
            fast = fast.next
        
        # if fast pointer is none then it has reached the end of the list
        # and the nth node to be removed from the end of the list is the head.
        if fast == None:
            return head.next
        
        while fast.next:
            fast, slow = fast.next, slow.next
        
        slow.next = slow.next.next
        return head