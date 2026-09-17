# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        low,high=-float('inf'),float('inf')

        def helper(root,low,high):
            if not root:
                return True
            if root.val<=low or root.val>=high:
                return False
            return helper(root.left,low,root.val) and \
                    helper(root.right,root.val,high)

        return helper(root,low,high)


if __name__ == '__main__':
    # t=TreeNode(2)
    # t.left=TreeNode(15)
    # t.right=TreeNode(3)
    t=TreeNode(5)
    t.left=TreeNode(1)
    t.right=TreeNode(4)
    t.right.left=TreeNode(3)
    t.right.right=TreeNode(6)
    sol=Solution()
    res=sol.isValidBST(t)
    print(res)