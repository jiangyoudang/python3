# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        imap = {}
        i = 0
        for val in inorder:
            imap[val] = i
            i += 1
        return self.recur(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, imap)



    def recur(self, preorder, pl, pr, inorder, il, ir, imap):
        if pl>pr or il>ir:
            return None
        root = TreeNode(preorder[pl])
        i_val = imap[root.val]
        root.left = self.recur(preorder, pl+1, pl+i_val-il, inorder, il, i_val-1, imap)
        root.right = self.recur(preorder, pl+i_val-il+1,pr, inorder, i_val+1,ir, imap)
        return root
