from collections import deque

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
        # if not root:
        #     return False
        # q=deque([(root,root.val)])
        # while q:
        #     curr_node,path_sum=q.popleft()
        #     if not curr_node.left and \
        #         not curr_node.right and \
        #         path_sum==targetSum:
        #         return True
        #     if curr_node.left:
        #         q.append((curr_node.left,path_sum+curr_node.left.val))
        #     if curr_node.right:
        #         q.append((curr_node.right,path_sum+curr_node.right.val))

        # return False

        if not root:
            return False
        
        def dfs(root,path_sum):
            if not root:
                return False
            
            path_sum+=root.val
            if not root.left and not root.right and \
                path_sum==targetSum:
                return True
                
            return dfs(root.left,path_sum) or \
                dfs(root.right,path_sum)

        return dfs(root,0)

if __name__ == '__main__':
    # t=TreeNode(5)
    # t.left=TreeNode(4)
    # t.left.left=TreeNode(11)
    # t.left.left.left=TreeNode(7)
    # t.left.left.right=TreeNode(2)
    # targetSum=22
    # t=TreeNode(1)
    # t.left=TreeNode(2)
    # t.right=TreeNode(3)
    # targetSum=4
    # t=None
    # t=TreeNode(1)
    # t.left=TreeNode(2)
    # targetSum=1
    sol=Solution()
    res=sol.hasPathSum(t,targetSum)
    print(res)