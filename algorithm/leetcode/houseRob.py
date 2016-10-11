# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def rob(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    return max(self.robMax(root))

  def robMax(self, root):
    if not root:
      return 0, 0
    robleft, left = self.robMax(root.left)
    robright, right = self.robMax(root.right)
    return left + right + root.val, max(left, robleft) + max(right, robright)
