'''
https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head)
    
    def helper(self, node, prev=None):
        if node == None:
            return prev
        
        curr = node.next
        node.next = prev
        return self.helper(curr, node)