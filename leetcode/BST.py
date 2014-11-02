from pprint import pprint
import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean

    #valid BST
    def isValidBST(self, root):
        pre = [None]
        return self.pre_order(root, pre)

    def pre_order(self, root, pre):
        if not root:
            return True
        left = self.pre_order(root.left, pre)
        print(root.val, pre[0])
        if pre[0] is not None and root.val<=pre[0]:
            return False

        pre[0] = root.val
        return left and self.pre_order(root.right,pre)

    #recover BST
    def recoverTree(self, root):
        pre = [None]
        swap1 = [None]
        swap2 = [None]
        self.pre_order2(root, pre, swap1, swap2)

        if swap1[0] and swap2[0]:
            swap1[0].val, swap2[0].val = swap2[0].val, swap1[0].val

        return root

    def pre_order2(self, root, pre, swap1, swap2):
        if root:
            self.pre_order2(root.left, pre, swap1, swap2)
            if pre[0] is not None and root.val <=pre[0].val:
                if swap1[0] is not None:
                    swap2[0] = root
                else:
                    swap1[0] = pre[0]
                    swap2[0] = root

            pre[0] = root

            self.pre_order2(root.right, pre, swap1, swap2)

    #unique BST 2
    def build(self, nodes):
        n = len(nodes)
        if n == 0:
            yield None
            return
        for i in range(n):
            root = nodes[i]
            for left in self.build(nodes[:i]):
                for right in self.build(nodes[i+1:]):
                    root.left, root.right = left, right
                    yield root

    # @return a list of tree node
    def generateTrees(self, n):
        nodes = map(TreeNode, range(1, n + 1))
        return map(copy.deepcopy, self.build(nodes))



    def sortedArrayToBST(self, num):
        n = len(num)
        mid = n//2
        if n==0:
            return None
        curr = TreeNode(num[mid])
        curr.left = self.sortedArrayToBST(num[:mid])
        curr.right = self.sortedArrayToBST(num[mid+1:])
        return curr

    def sortedListToBST(self, head):
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1
        pre = [head]
        return self.listToBST_2(pre, 0, n-1)

    def listToBST_2(self, pre, l, r):
        if l>r:
            return None
        mid = (l+r)//2
        left = self.listToBST_2(pre, l, mid-1)
        curr = TreeNode(pre[0].val)
        pre[0] = pre[0].next
        curr.left = left
        curr.right = self.listToBST_2(pre, mid+1, r)
        return curr



root = TreeNode(2)
root.right = TreeNode(1)
root.left = TreeNode(3)

test = Solution().recoverTree(root)
pprint(root.val)
pprint(root.left.val)
pprint(root.right.val)
