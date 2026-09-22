class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    memo[i]=max(memo[i],memo[j]+1)

        return max(memo)


if __name__ == '__main__':
    nums=[10,9,2,5,3,7,101,18]
    sol=Solution()
    res=sol.lengthOfLIS(nums)
    print(res)