# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        p2 = headB
        count1 = 0
        count2 = 0
        while p1 or p2:
            if p1:
                p1 = p1.next
                count1 += 1
            if p2:
                p2 = p2.next
                count2 += 1
        p1 = headA
        p2 = headB
        count = count2-count1
        while count>0:
            p2 = p2.next
            count -= 1
        while count<0:
            p1 = p1.next
            count += 1
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
        return p1

