class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        track=[]
        n=len(nums)
        def helper(track,depth):
            # if depth>n:
            #     return
            if depth==n:
                res.append(track[:])
                return
            # Make choice: inclusion
            track.append(nums[depth])
            # Backtrack children
            helper(track,depth+1)
            # Undo choice
            track.pop()

            # Make choice: exclusion
            # Backtrack children
            helper(track,depth+1)

        helper(track,0)
        return res


if __name__ == '__main__':
    nums=[1,2,3]
    sol=Solution()
    res=sol.subsets(nums)
    print(res)