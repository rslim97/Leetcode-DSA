class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums))!=len(nums)
        

if __name__ == '__main__':
    sol=Solution()
    nums=[1,1,1]
    res=sol.containsDuplicate(nums)
    print(res)