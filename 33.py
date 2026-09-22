class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            mid_val=nums[mid]
            if mid_val==target:
                return mid
            # In non-decreasing order part
            elif mid_val>=nums[l]:
                if nums[l]<=target<mid_val:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if mid_val<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1

        return -1


if __name__ == '__main__':
    nums=[4,5,6,7,0,1,2]
    target=3
    sol=Solution()
    res=sol.search(nums,target)
    print(res)