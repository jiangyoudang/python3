#  O(1) Space
from lib.prettyBST import prettyBST
class treeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def test_tree():
    tree = {i:treeNode(i) for i in range(1,11)}
    tree[1].left = tree[2]
    tree[1].right = tree[3]
    tree[2].left = tree[4]
    tree[2].right = tree[6]
    tree[4].right = tree[5]
    tree[6].left = tree[7]
    tree[3].right = tree[8]
    tree[8].right = tree[10]
    tree[8].left = tree[9]

    return tree[1]

def preorder(root):
    curr = root
    res = []
    while curr:

        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            predecessor = curr.left
            while predecessor.right and predecessor.right != curr:
                predecessor = predecessor.right
            if not predecessor.right:
                res.append(curr.val)
                predecessor.right = curr
                curr = curr.left
            else:
                predecessor.right = None
                curr = curr.right

    return res

def inorder(root):
    curr = root
    res = []

    while curr:
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right
            if not pre.right:
                pre.right = curr
                curr = curr.left
            else:
                res.append(curr.val)
                pre.right = None
                curr = curr.right

    return res

def preorder_stack(root):
    if not root:
        return root

    stack = [root]
    res = []
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res

def inorder_stack(root):
    if not root:
        return root
    stack = []
    res = []
    curr = root
    while curr or stack:
        if not curr:
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        else:
            stack.append(curr)
            curr = curr.left

    return res

root = test_tree()
prettyBST(root)
print(inorder(root))
print(inorder_stack(root))
