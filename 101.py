# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return root1.val==root2.val and \
                helper(root1.left,root2.right) and \
                helper(root1.right,root2.left)

        return helper(root,root)        


if __name__ == '__main__':
    t=TreeNode(1)
    # t.left=TreeNode(2)
    # t.right=TreeNode(3)
    sol=Solution()
    res=sol.isSymmetric(t)
    print(res)