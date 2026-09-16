# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inOrderTraversal(root):
    res=[]
    def helper(root):
        if not root:
            return
        helper(root.left)
        res.append(root.val)
        helper(root.right)
    helper(root)
    return res   

def preOrderTraversal(root):
    res=[]
    def helper(root):
        if not root:
            return
        res.append(root.val)
        helper(root.left)
        helper(root.right)
    helper(root)
    return res

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

if __name__ == '__main__':
    r=TreeNode(4)
    r.left=TreeNode(2)
    r.right=TreeNode(7)
    r.left.left=TreeNode(1)
    r.left.right=TreeNode(3)
    r.right.left=TreeNode(6)
    r.right.right=TreeNode(9)
    sol=Solution()
    res=sol.invertTree(r)
    res=inOrderTraversal(r)
    print(res)
    res=preOrderTraversal(r)
    print(res)