# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        res=[]
        return res


if __name__ == '__main__':
    t=TreeNode(1)
    t.left=TreeNode(2)
    t.left.right=TreeNode(5)
    t.right=TreeNode(3)
    sol=Solution()
    res=sol.binaryTreePaths(t)
    print(res)