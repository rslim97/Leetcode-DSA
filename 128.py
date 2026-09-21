class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen=set(nums)
        longest_streak=0
        for num in nums:
            if num-1 not in seen:
                curr_num=num
                streak=1
                while curr_num+1 in seen:
                    curr_num+=1
                    streak+=1
                longest_streak=max(longest_streak,streak)

        return longest_streak


if __name__ == '__main__':
    nums=[100,4,200,1,3,2]
    sol=Solution()
    res=sol.longestConsecutive(nums)
    print(res)