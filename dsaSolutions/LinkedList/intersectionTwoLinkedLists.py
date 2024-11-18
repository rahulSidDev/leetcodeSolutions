'''
https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        
        pa = headA
        pb = headB
        
        while pa != pb:
            pa = headB if pa == None else pa.next
            pb = headA if pb == None else pb.next
            
        return pa