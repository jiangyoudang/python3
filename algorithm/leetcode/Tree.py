from algorithm.lib import pretty_tree


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.root_pos = 0
        self.preorder = preorder
        in_map = {v: k for k, v in enumerate(inorder)}
        self.in_map = in_map
        return self.helper(0, len(inorder)-1)

    def helper(self, l, r):
        if l > r:
            return None
        root = TreeNode(self.preorder[self.root_pos])
        root_index = self.in_map[self.preorder[self.root_pos]]
        self.root_pos += 1
        root.left = self.helper(l, root_index-1)
        root.right = self.helper(root_index+1, r)
        return root



preorder = [1, 2, 3]
inorder = [2, 1, 3]
root = Solution().buildTree(preorder, inorder)
pretty_tree.prettyBST(root)
