from collections import deque

class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def dep(root):
    if not root:
        return 0
    return max(dep(root.left), dep(root.right)) + 1


def pretty_BT(root):
    if not root:
        return ''
    curr_level = [root]
    next_level = []
    h = dep(root)
    space_length = (1 << h) - 1
    while curr_level:
        if not any(curr_level):
            break

        print(' '*(space_length>>1), end = '')
        for node in curr_level:
            if not node:
                print(' ', end='')
                print(' '*space_length, end = '')
                continue
            print(node.val, end='')
            next_level.append(node.left)
            next_level.append(node.right)
            if node == curr_level[-1]:
                print('')
                space_length >>= 1
            else:
                print(' '*space_length, end = '')
        curr_level = next_level
        next_level = []



root = node(1)
root.left = node(2)
root.right = node(3)
root.right.left = node(4)

pretty_BT(root)





