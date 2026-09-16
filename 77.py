class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        track=[]
        def helper(track,depth):
            # Termination condition
            if depth>n+1:
                return
            if len(track)==k:
                res.append(track[:])
                return
            # Make choice: inclusion
            track.append(depth)
            # Backtrack
            helper(track,depth+1)
            # Undo choice
            track.pop()

            # Make choice: exclusion
            # Backtrack
            helper(track,depth+1)

        helper(track,1)
        return res


if __name__ == '__main__':
    n,k=4,2
    sol=Solution()
    res=sol.combine(n,k)
    print(res)