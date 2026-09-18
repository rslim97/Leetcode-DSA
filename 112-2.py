# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        def helper(path_sum,root):
            if not root:
                return False
            path_sum+=root.val
            if not root.left and not root.right and \
                path_sum==targetSum:
                return True
            return helper(path_sum,root.left) or \
                helper(path_sum,root.right)

        return helper(0,root)


if __name__ == '__main__':
    t=TreeNode(5)
    t.left=TreeNode(4)
    t.left.left=TreeNode(11)
    t.left.left.left=TreeNode(7)
    t.left.left.right=TreeNode(2)
    t.right=TreeNode(8)
    t.right.left=TreeNode(13)
    t.right.right=TreeNode(4)
    t.right.right.right=TreeNode(1)
    targetSum=21
    sol=Solution()
    res=sol.hasPathSum(t,targetSum)
    print(res)