# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """

        def dfs(root,low,high):
            range_sum=0
            if not root:
                return 0
            if low<=root.val<=high:
                range_sum+=root.val
            if root.left:
                range_sum+=dfs(root.left,low,high)
            if root.right:
                range_sum+=dfs(root.right,low,high)

            return range_sum
        
        return dfs(root,low,high)


if __name__ == '__main__':
    t=TreeNode(10)
    t.left=TreeNode(5)
    t.left.left=TreeNode(3)
    t.left.right=TreeNode(7)
    t.right=TreeNode(15)
    t.right.right=TreeNode(18)
    low,high=7,15
    t=TreeNode(10)
    t.left=TreeNode(5)
    t.left.left=TreeNode(3)
    t.left.right=TreeNode(7)
    t.left.left.left=TreeNode(1)
    t.left.right.left=TreeNode(6)
    t.right=TreeNode(15)
    t.right.left=TreeNode(13)
    t.right.right=TreeNode(18)
    low,high=6,10
    sol=Solution()
    res=sol.rangeSumBST(t,low,high)
    print(res)