'''
https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/
'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        
        return True