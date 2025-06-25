'''
https://leetcode.com/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            # if both input nodes are None then they are the same and true is returned.
            if p == None and q == None:
                return True
            # if one of the nodes is not none then they are different and false is returned.
            if p == None or q == None:
                return False
            # if the values of the two nodes are different then the nodes are different and 
            # false is returned.
            if p.val != q.val:
                return False

            # if none of the above conditions are fulfilled then the nodes are the same.
            return True
        
        # create a double ended queue with the root input nodes as the initial pair of 
        # elements in the dequeue.
        deq = deque([(p, q),])
        # iterate until dequeue is empty.
        while deq:
            # get the current p and q nodes from the queue.
            p, q = deq.popleft()
            # pass both nodes to the check function and if false is returned then
            # the two BTs are not the same and false is returned.
            if not check(p,q):
                return False
            # otherwise add two pairs to the dequeue which contain the left nodes and 
            # the right nodes of both BTs respectively.
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        
        # return true if no difference between the two BTs is found.
        return True
