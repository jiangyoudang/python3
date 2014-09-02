__author__ = 'congliu'
import unittest

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# method 1
def postorder(root):
    '''
    use Predecessor.right = cur
    '''
    result = []
    dump = TreeNode('start')
    dump.left = root
    curr = dump
    while curr:
        if not curr.left:
            curr = curr.right
        else:
            # find predecessor
            predecessor = curr.left
            while predecessor.right and not predecessor.right == curr:
                predecessor = predecessor.right
            if not predecessor.right:
                predecessor.right = curr
                curr = curr.left

            # predecessor.right == curr
            else:

                # reversely output from curr.left to predecessor
                temp = []
                x = curr.left
                y = predecessor
                while not x == y:
                    temp.append(x.val)
                    x = x.right
                temp.append(y.val)
                while temp:
                    result.append(temp.pop())

                # curr = curr.right
                predecessor.right = None
                curr = curr.right

    return result

# method 2
def postorder2(root):
    '''
    Use one additional flag prev
    '''
    result = []
    stack = [root]
    prev = None
    while stack:
        curr = stack[-1]
        if not prev or prev.right == curr or prev.left == curr:
            if curr.left:
                stack.append(curr.left)
            elif curr.right:
                stack.append(curr.right)
            else:
                result.append(stack.pop().val)
        elif curr.left == prev:
            if curr.right:
                stack.append(curr.right)
            else:
                result.append(stack.pop().val)
        else:
            result.append(stack.pop().val)

        prev = curr

    return result

# method 3
def postorder3(root):
    '''
    Use 2 stacks
    '''
    stack1 = [root]
    stack2 = []
    result = []
    while stack1:
        curr = stack1.pop()
        stack2.append(curr)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)

    # output reverse of stack2
    while stack2:
        result.append(stack2.pop().val)

    return result


class Test(unittest.TestCase):

    # def test_empty(self):
    #     root = [None]
    #
    #     self.assertEqual(postorder(root),[None])
    #     self.assertEqual(postorder2(root),[None])
    #     self.assertEqual(postorder3(root),[None])

    def test_Tree(self):
        root = TreeNode(1)

        self.assertEqual(postorder(root),[1])
        self.assertEqual(postorder2(root),[1])
        self.assertEqual(postorder3(root),[1])

    def test_tree2(self):
        left = TreeNode(2,None,TreeNode(4,TreeNode(5)))
        right = TreeNode(3,TreeNode(6,None,TreeNode(8)),TreeNode(7))
        root = TreeNode(1,left,right)

        res = [5,4,2,8,6,7,3,1]
        self.assertEqual(postorder(root),res)
        self.assertEqual(postorder2(root),res)
        self.assertEqual(postorder3(root),res)

unittest.main()
#print(postorder(root))