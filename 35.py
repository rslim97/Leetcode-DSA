class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return l
    

if __name__ == '__main__':
    nums=[1,3,5,6]
    target=5
    target=2
    nums = [1,3,5,6]
    target=7
    sol=Solution()
    res=sol.searchInsert(nums,target)
    print(res)