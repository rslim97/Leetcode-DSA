class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Transpose matrix
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        # Reverse each row
        for i in range(n):
            # matrix[i].reverse()
            matrix[i][:]=matrix[i][::-1]
        return matrix


if __name__ == '__main__':
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    sol=Solution()
    res=sol.rotate(matrix)
    print(res)