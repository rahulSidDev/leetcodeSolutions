'''
https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                
                return slow
        
        return None