class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i,j,k=m-1,n-1,m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1 


if __name__ == '__main__':
    nums1=[1,2,3,0,0,0]
    nums2=[2,5,6]
    m=3
    n=3
    nums1=[1]
    m=1
    nums2=[]
    n=0

    sol=Solution()
    res=sol.merge(nums1,m,nums2,n)
    print(nums1)    