'''
https://leetcode.com/problems/reverse-nodes-in-k-group/description/?envType=study-plan-v2&envId=top-interview-150
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, left, right):
        endP = right.next
        currP = endP
        firstLeft = left
        while left != endP:
            nextN = left.next
            left.next = currP
            currP = left
            left = nextN

        return firstLeft, right

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # create a dummy head just before the list head because the real head will change as the list is manipulated.
        dummyHead = ListNode(0, head)
        # create the iterator pointer at the head of the list.
        currNode = dummyHead.next
        # create a left pointer to keep track of the node just before the sublist to be reversed.
        leftP = dummyHead
        # variable to store the node number.
        nodeCount = 0

        # iterate through the list until the end
        while currNode:
            # increment the node number when a new node is reached at the start of a new iteration.
            nodeCount += 1
            # if nodecount becomes a multiple of k then that means the sublist needs to be reversed.
            if nodeCount % k == 0:
                # save the current node pointer as the pointer to the rightmost node of the sublist to be reversed.
                rightP = currNode
                # call the reverselist function by passing in the pointers to the left and right nodes of the sublist to be reversed.
                # get back left and right node pointers of the reversed sublist and update the current node pointer to be the rightmost
                # node of the reversed sublist and connect the node just before the reversed sublist to the leftmost node of the reversed
                # sublist.
                currNode, leftP.next = self.reverseList(leftP.next, rightP)
                # update the pointer to the node just before the next sublist to be reversed.
                leftP = currNode

            # updated the current node pointer to the next node.
            currNode = currNode.next
        
        # return the head using the dummyHead's next node.
        return dummyHead.next
