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
        # res=[]
        # track=[]
        # def helper(track,root):
        #     if not root:
        #         return
        #     # Make choice
        #     track.append(root.val)
        #     # Detect leaf node
        #     if not root.left and not root.right:
        #         res.append(track[:])
        #     helper(track,root.left)
        #     helper(track,root.right)
        #     # Undo choice/backtrack
        #     track.pop()

        # helper(track,root)
        # return res

        res=[]
        track=""
        def helper(track,root):
            if not root:
                return
            # Make choice
            track+=str(root.val)
            if not root.left and not root.right:
                res.append(track[:])
            helper(track+"->",root.left)
            helper(track+"->",root.right)
            # Undo choice
            track=track[:-1]

        helper(track,root)
        return res
    

if __name__ == '__main__':
    t=TreeNode(1)
    t.left=TreeNode(2)
    t.left.right=TreeNode(5)
    t.right=TreeNode(3)
    sol=Solution()
    res=sol.binaryTreePaths(t)
    print(res)