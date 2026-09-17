class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h,w=len(grid),len(grid[0])
        visited=[[False]*w for _ in range(h)]
        def dfs(i,j):
            perimeter=0
            # Base case
            ## Check bounds
            if i<0 or i>=h or j<0 or j>=w:
                return 1
            ## Check bounds
            if grid[i][j]==0:  # To deal with water
                return 1
            ## Check if visited
            if visited[i][j]:  # To deal with land
                return 0
            # Mark visited
            visited[i][j]=True
            # Recursive case
            perimeter+=dfs(i+1,j)
            perimeter+=dfs(i-1,j)
            perimeter+=dfs(i,j+1)
            perimeter+=dfs(i,j-1)
            return perimeter

        for i in range(h):
            for j in range(w):
                if grid[i][j]==1:
                    return dfs(i,j)


if __name__ == '__main__':
    grid=[[1]]
    grid=[[1,0]]
    grid=[[0,1,0,0],
          [1,1,1,0],
          [0,1,0,0],
          [1,1,0,0]]
    sol=Solution()
    res=sol.islandPerimeter(grid)
    print(res)