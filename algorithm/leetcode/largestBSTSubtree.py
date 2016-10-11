from algorithm.lib.data_structure import TreeNode


class Solution(object):
  def largestBSTSubtree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
      return 0
    self.largest = 0
    self.helper(root)
    return self.largest

  def helper(self, root):
    if not root:
      return 0, float('inf'), float('-inf')
    left, left_min, left_max = self.helper(root.left)
    right, right_min, right_max = self.helper(root.right)

    if left == -1 or right == -1 or not left_max < root.val < right_min:
      return -1, None, None
    root_min = root_max = root.val
    if left:
      root_min = left_min
    if right:
      root_max = right_max

    subtree_num = 1 + left + right
    if subtree_num > self.largest:
      self.largest = subtree_num
    return 1 + left + right, root_min, root_max
