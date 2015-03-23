from lib.prettyBST import treeNode, pretty_BST
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
    #todo
    pass

test = make_test()
print(test)
root = max_tree1(test)

pretty_BST(root)
