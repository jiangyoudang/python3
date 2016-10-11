from algorithm.lib.pretty_tree import prettyBST
from algorithm.lib.data_structure import TreeNode

root = TreeNode(4)
root.right = TreeNode(1)
root.left = TreeNode(7)
root.left.left = TreeNode(8)

head = root

def ToBST(root):
  if not root:
    return

  left = root.left
  right = root.right

  root.left = root.right = None
  insert(root)

  ToBST(left)
  ToBST(right)

def insert(root):
  if root == head:
    return
  curr = head
  while True:
    if root.val < curr.val:
      if not curr.left:
        curr.left = root
        return
      curr = curr.left
    elif root.val > curr.val:
      if not curr.right:
        curr.right = root
        return
      curr = curr.right



prettyBST(root)
ToBST(root)
prettyBST(head)

