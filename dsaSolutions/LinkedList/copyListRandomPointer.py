'''
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/
'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        curr = head
        while curr:
            newNode = Node(curr.val, curr.next)
            curr.next = newNode
            curr = newNode.next
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        newHead = head.next
        oldHead = head
        currNew = newHead
        currOld = oldHead
        while currOld:
            currOld.next = currOld.next.next
            currNew.next = currNew.next.next if currNew.next else None
            currOld = currOld.next
            currNew = currNew.next
            
        return newHead