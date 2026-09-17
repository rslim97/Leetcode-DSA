# -*- coding: utf-8 -*-
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        q1=deque([p])
        q2=deque([q])
        while len(q1)>0 and len(q2)>0:
            node_p=q1.popleft()
            node_q=q2.popleft()
            if not node_p and not node_q:
                continue
            if not node_p or not node_q:
                return False
            if node_p.val!=node_q.val:
                return False
            q1.append(node_p.left)
            q1.append(node_p.right)
            q2.append(node_q.left)
            q2.append(node_q.right)
        return True
        
        
if __name__ == '__main__':
    p=TreeNode(1)
    # p.left=TreeNode(2)
    q=TreeNode(2)
    # q.right=TreeNode(2)
    sol=Solution()
    res=sol.isSameTree(p, q)
    print(res)