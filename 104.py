# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and root.right:
            return 1+self.maxDepth(root.right)
        if root.left and not root.right:
            return 1+self.maxDepth(root.left)
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))


if __name__ == '__main__':
    # t=TreeNode(3)
    # t.left=TreeNode(9)
    # t.right=TreeNode(20)
    # t.right.left=TreeNode(15)
    # t.right.right=TreeNode(7)
    t=TreeNode(1)
    t.right=TreeNode(2)
    sol=Solution()
    res=sol.maxDepth(t)
    print(res)