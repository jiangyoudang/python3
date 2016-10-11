from algorithm.lib.pretty_tree import treeNode, prettyBST, treePrint, lalala
from random import shuffle

def make_test():
    a = [i for i in range(10)]
    shuffle(a)
    return a


def max_tree1(a):

    if not a:
        return None

    m = max(a)
    i = a.index(m)
    root = treeNode(a[i])
    root.left = max_tree1(a[:i])
    root.right = max_tree1(a[i+1:])

    return root

def max_tree2(a):
    nodes = [treeNode(i) for i in a]
    stack = []
    curr = None
    for e in nodes:
        while stack and e.val > stack[-1].val:
            curr = stack.pop()
            left_larger = float('inf') if not stack else stack[-1].val
            if e.val > left_larger:
                stack[-1].right = curr
            else:
                e.left = curr
        stack.append(e)

    while stack:
        curr = stack.pop()
        if stack:
            stack[-1].right = curr

    return curr


def splitTree(root, target, Large, Small):
    if not root:
        # Large[0] = Small[0] = None
        return

    if root.val > target:
        # large = root
        leftLarge = [None]
        leftSmall = [None]
        splitTree(root.left, target, leftLarge, leftSmall)
        root.left = leftLarge[0]
        Large[0] = root
        Small[0] = leftSmall[0]
    elif root.val < target:
        rightLarge = [None]
        rightSmall = [None]
        splitTree(root.right, target, rightLarge, rightSmall)
        root.right = rightSmall[0]
        Large[0] = rightLarge[0]
        Small[0] = root
    else:
        Large[0] = root.right
        Small[0] = root
        root.right = None
#
test = make_test()
print(test)
root = max_tree1(test)
treePrint(root, 3)

print(lalala)
root2 = max_tree2(test)
treePrint(root, 3)


#
# pretty_BST(root)
root = treeNode(3)
root.left = treeNode(-2)
root.right = treeNode(4)
root.left.left = treeNode(-3)
root.left.right = treeNode(1)
#
# large = [None]
# small = [None]
# splitTree(root, 0, large, small)
# prettyBST(large[0])
# print('--------lalala------')
# prettyBST(small[0])