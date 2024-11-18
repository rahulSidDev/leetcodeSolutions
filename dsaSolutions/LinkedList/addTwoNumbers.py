'''
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0
        
        while l1 != None or l2 != None or carry != 0:
            digit1 = l1.val if l1 != None else 0
            digit2 = l2.val if l2 != None else 0
            
            summ = digit1 + digit2 + carry
            unitdigit = summ % 10
            carry = summ // 10
            
            tail.next = ListNode(unitdigit)
            tail = tail.next
            
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        
        return dummyHead.next