class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]>=nums[mid+1]:
                r=mid
            else:
                l=mid+1

        return l
    

if __name__ == '__main__':
    nums=[1,2,3,1]
    sol=Solution()
    res=sol.findPeakElement(nums)
    print(res)