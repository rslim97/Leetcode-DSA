class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        h,w=len(matrix),len(matrix[0])
        for i in range(1,h):
            for j in range(1,w):
                if matrix[i][j]!=matrix[i-1][j-1]:
                    return False

        return True
    

if __name__ == '__main__':
    matrix=[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    sol=Solution()
    res=sol.isToeplitzMatrix(matrix)
    print(res)