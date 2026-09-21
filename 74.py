class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        h,w=len(matrix),len(matrix[0])
        l,r=0,h*w-1
        while l<=r:
            mid=l+(r-l+1)//2
            mid_value=matrix[mid//w][mid%w]
            if mid_value==target:
                return True
            elif target<mid_value:
                r=mid-1
            else:
                l=mid+1

        return False


if __name__ == '__main__':
    matrix=[[1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]]
    target=30
    sol=Solution()
    res=sol.searchMatrix(matrix,target)
    print(res)