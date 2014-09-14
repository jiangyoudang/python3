# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer

    def maxPathSum(self, root):
        max_accross_root = [float('-inf')]
        max_end_root = self.getMax(root, max_accross_root)
        return max(max_end_root, max_accross_root[0])

    def getMax(self, root, max_accross_root):
        if not root:
            return 0
        left = self.getMax(root.left, max_accross_root)
        right = self.getMax(root.right, max_accross_root)

        max_val = max(root.val, root.val+left, root.val+right, root.val+left+right)
        max_accross_root[0] = max(max_val, max_accross_root[0])

        return max(root.val, root.val+left, root.val+right)