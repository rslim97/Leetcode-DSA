class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo=[0]*len(nums)
        memo[0]=nums[0]
        for i in range(1,len(nums)):
            if memo[i-1]>0:
                # Extend subarray
                memo[i]=memo[i-1]+nums[i]
            else:
                # nums[i] as start of a new subarray
                memo[i]=nums[i]

        return max(memo)

        # curr_sum=0
        # max_sum=-float('inf')
        # for i in range(len(nums)):
        #     curr_sum+=nums[i]
        #     max_sum=max(max_sum,curr_sum)
        #     if curr_sum<0:
        #         curr_sum=0

        # return max_sum
        

if __name__ == '__main__':
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    nums=[1]
    nums=[5,4,-1,7,8]
    sol=Solution()
    res=sol.maxSubArray(nums)
    print(res)