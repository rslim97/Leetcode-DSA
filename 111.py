from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        q=deque([(root, 1)])
        while q:
            curr_node,level=q.popleft()
            if not curr_node.left and not curr_node.right:
                return level
            if curr_node.left:
                q.append((curr_node.left,level+1))
            if curr_node.right:
                q.append((curr_node.right,level+1))

        return level

        # if not root:
        #     return 0
        # if not root.left and root.right:
        #     return 1+self.minDepth(root.right)
        # if root.left and not root.right:
        #     return 1+self.minDepth(root.left)
        # return 1+min(self.minDepth(root.left),self.minDepth(root.right))

    

if __name__ == "__main__":
    # t=TreeNode(3)
    # t.left=TreeNode(9)
    # t.right=TreeNode(20)
    # t.right.left=TreeNode(15)
    # t.right.right=TreeNode(7)
    t=TreeNode(2)
    t.right=TreeNode(3)
    t.right.right=TreeNode(4)
    t.right.right.right=TreeNode(5)
    t.right.right.right.right=TreeNode(6)
    sol=Solution()
    res=sol.minDepth(t)
    print(res)
        