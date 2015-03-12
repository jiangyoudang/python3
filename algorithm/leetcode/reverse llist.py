# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m==n:
            return head
        pre_head = ListNode(1)
        pre_head.next = head


        #get pre_m and pre_n
        pre = pre_head
        for i in range(m-1):
            pre = pre.next
        pre_m = pre
        curr = pre_m.next
        temp = None
        for i in range(n-m+1):
            pnext = curr.next
            curr.next = temp
            temp = curr
            curr = pnext

        pre_m.next.next = curr
        pre_m.next = temp

        return pre_head.next



head = ListNode(5)
head.next = ListNode(3)
print(head)
print(Solution().reverseBetween(head,1,2))