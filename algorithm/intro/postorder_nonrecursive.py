__author__ = 'congliu'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def postorderTraversal(root):
    if not root:
        return None
    stack = [root]
    result = []
    cache = []
    while stack:
        root = stack[-1]
        if root.left in cache:
            root.left = None
        if root.right in cache:
            root.right = None
        while root.right or root.left:
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            root = stack[-1]
    #while root:
        current = stack.pop()
        result.append(current.val)
        cache.append(current)


    return result


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(postorderTraversal(root))

