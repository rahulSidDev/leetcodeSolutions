'''
https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/
'''
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        odd = head
        even = head.next
        evenhead = even
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = evenhead
        return head