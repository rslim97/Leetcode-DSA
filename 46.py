class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]  # Result
        track=[]  # Track
        used=[False]*len(nums)  # Choice list
        def helper(track,used):
            # Termination condition
            if len(track)==len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Make choice
                used[i]=True
                track.append(nums[i])
                # Backtrack children
                helper(track,used)
                # Undo choice
                used[i]=False
                track.pop()                                

        helper(track,used)
        return res


if __name__ == '__main__':
    nums=[1,2,3]
    sol=Solution()
    res=sol.permute(nums)
    print(res)
