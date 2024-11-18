'''
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/
'''
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        
        lastElement = head
        length = 1
        while lastElement.next:
            lastElement = lastElement.next
            length += 1
            
        k = k % length
        lastElement.next = head
        
        tempNode = head
        for _ in range(length-k-1):
            tempNode = tempNode.next
        
        ansNode = tempNode.next
        tempNode.next = None
        
        return ansNode