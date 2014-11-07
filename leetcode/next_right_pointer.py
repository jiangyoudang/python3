
# class TreeNode:
def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
    self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        head = None
        mover = None
        curr = root

        while curr:
            while curr:
                if curr.left:
                    if not mover:
                        mover = curr.left
                        head = curr.left
                    else:
                        mover.next = curr.left
                        mover = mover.next
                if curr.right:
                    if not mover:
                        mover = curr.left
                        head = curr.left
                    else:
                        mover.next = curr.right
                        mover = mover.next
                curr = curr.next
            mover = None
            curr = head
            head = None