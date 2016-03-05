class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.root = root
        h = 0
        curr = root
        while curr:
            h += 1
            curr = curr.left
        left = 1
        right = 1 << (h-1)
        while left <= right:
            mid = (left+right) >> 1
            if self.getNode(mid, h):
                left += 1
            else:
                right -= 1
        return (1 << (h-1)) - 1+ right
            
            
    def getNode(self, i, h):
        finder = self.root
        while h > 1:
            if i > (1 << (h-2)):
                finder = finder.right
                i -= (1 << (h-2))
            else:
                finder = finder.left
            h -= 1
        return finder


if 3&1:
    print('odd')
elif 0&1:
    print('even')