class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # def helper(low,high):
        #     while low<=high:
        #         mid=low+(high-low+1)//2
        #         if nums[mid]==target:
        #             return mid
        #         elif target<nums[mid]:
        #             high=mid-1
        #         else:
        #             low=mid+1

        #     return -1
        
        # return helper(0,len(nums)-1)

        # l,r=0,len(nums)-1
        # def helper(l,r):
        #     if l<=r:
        #         mid=l+(r-l+1)//2
        #         # print(l,mid,r)
        #         if nums[mid]==target:
        #             return mid
        #         if target<nums[mid]:
        #             return helper(l,mid-1)
        #         else:
        #             return helper(mid+1,r)
        #     else:
        #         return -1
        # return helper(l,r)

        l,r=0,len(nums)-1
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]>=target:
                r=mid
            else:
                l=mid+1

        return l if nums[l]==target else -1


if __name__== '__main__':
    nums=[-1,0,3,5,9,12]
    target=9
    nums=[-1,0,3,5,9,12]
    target=2
    nums=[5]
    target=5
    sol=Solution()
    res=sol.search(nums,target)
    print(res)
