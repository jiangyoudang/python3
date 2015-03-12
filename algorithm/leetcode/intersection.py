# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        p2 = headB
        if not (headB and headA):
            return None
        while p2.next:
            p2 = p2.next
        p2.next = headB
        p3 = p2
        p1 = headA.next
        if not(headA and headA.next):
            p3.next = None
            return None

        p2 = headA.next.next
        while p2 and p2.next and p2.next.next and p1!=p2:
            p1 = p1.next
            p2 = p2.next.next
        if not (p2 and p2.next and p2.next.next):
            p3.next = None
            return None
        p2 = headA
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
        p3.next = None
        return p1


headA = ListNode(1)
headA.next = ListNode(3)

headB = ListNode(2)
headB.next = ListNode(4)
headB.next.next = ListNode(6)

print(Solution().getIntersectionNode(headA,headB))
