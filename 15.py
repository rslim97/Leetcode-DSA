class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            # If nums[i] is positive that means we can no longer produce a 0, break.
            if nums[i]>0:
                break
            # Skip to next if nums[i] is the same number as we've previously tried.
            if i>0 and nums[i]==nums[i-1]:
                continue
            j,k=i+1,len(nums)-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]

                if total<0:
                    j+=1
                elif total>0:
                    k-=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    # Increment j so that we arrive at a
                    # different number.
                    j+=1
                    # Similarly, decrement k to arrive at a
                    # different number.
                    k-=1

        return res


if __name__ == '__main__':
    nums=[-1,0,1,2,-1,-4]
    # nums=[0,0,0]
    sol=Solution()
    res=sol.threeSum(nums)
    print(res)