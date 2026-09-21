class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major_elem=nums[0]
        counter=1
        for i in range(1,len(nums)):
            if nums[i]==major_elem:
                counter+=1
            else:
                counter-=1
                if counter==0:
                    major_elem=nums[i]
                    counter=1
        return major_elem


if __name__ == '__main__':
    nums=[1,1,2,1]
    nums=[2,2,1,1,1,2,2]
    # nums=[3,2,3]
    sol=Solution()
    res=sol.majorityElement(nums)
    print(res)