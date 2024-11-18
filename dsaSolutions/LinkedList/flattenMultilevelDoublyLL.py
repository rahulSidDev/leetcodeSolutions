'''
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/
'''
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        dummy = Node(0, None, head, None)
        stack = []
        stack.append(head)
        prev = dummy
        
        while stack:
            root = stack.pop()
            root.prev = prev
            prev.next = root
            
            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            
            prev = root
        
        dummy.next.prev = None
        return dummy.next