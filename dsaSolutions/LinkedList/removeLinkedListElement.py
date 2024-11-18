'''
https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/
'''
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None
        
        head.next = self.removeElements(head.next, val)
        return head if head.val != val else head.next