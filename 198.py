class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return nums[0]

        memo=[0]*(len(nums))
        memo[0]=nums[0]
        memo[1]=max(nums[0],nums[1])

        for i in range(2,len(nums)):
            memo[i]=max(memo[i-2]+nums[i],memo[i-1])

        return memo[len(nums)-1]


if __name__ == '__main__':
    nums=[1,2,3,1]
    sol=Solution()
    res=sol.rob(nums)
    print(res)