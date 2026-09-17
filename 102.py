from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[]
        q=deque([root])
        next_q=deque([])
        # The root node is considered as level 1
        depth=1
        while q:
            sz=len(q)
            sol=[]
            for i in range(sz):
                c=q.popleft()
                if c.left:
                    next_q.append(c.left)
                if c.right:
                    next_q.append(c.right)
                sol.append(c.val)
            res.append(sol[:])
            q=next_q
            next_q=deque([])
            depth+=1
        return res

if __name__ == '__main__':
    t=TreeNode(3)
    t.left=TreeNode(9)
    t.right=TreeNode(20)
    t.right.left=TreeNode(15)
    t.right.right=TreeNode(7)
    
    sol=Solution()
    res=sol.levelOrder(t)
    print(res)