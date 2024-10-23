'''
Given the roots of two binary trees 'p' and 'q', write a function to check if they are the same or not. Two binary trees 
are considered the same if they are structurally identical, and the nodes have the same value.
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if p == None and q == None:
                return True
            if p == None or q == None:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p,q):
                return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        
        return True