# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return None
        s = [root]
        p = root
        while s:
            curr = s.pop()
            if curr!=root:
                p.right = curr
                p.left = None
                p = curr
            if curr.right:
                s.append(curr.right)
            if curr.left:
                s.append(curr.left)
        return root

