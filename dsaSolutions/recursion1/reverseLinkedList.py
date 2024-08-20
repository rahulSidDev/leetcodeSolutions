"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head)
    
    def helper(self, node, prev=None):
        if node == None:
            return prev
        
        curr = node.next
        node.next = prev
        return self.helper(curr, node)