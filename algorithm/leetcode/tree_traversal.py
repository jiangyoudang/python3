import collections


class Solution(object):
  def verticalOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
      return []
    cols = collections.defaultdict(list)
    cols[0].append(root.val)
    left_col_num = 0
    queue = [(root, 0)]
    while queue:
      next_level = []
      for curr, col_num in queue:
        if curr.left:
          next_level.append((curr.left, col_num-1))
          cols[col_num-1].append(curr.left.val)
          if left_col_num > col_num-1:
            left_col_num = col_num-1
        if curr.right:
          next_level.append((curr.right, col_num+1))
          cols[col_num+1].append(curr.right.val)
      queue = next_level

    # get result
    result = [0] * len(cols)
    for key in cols:
      result[key-left_col_num] = cols[key]
    return result

