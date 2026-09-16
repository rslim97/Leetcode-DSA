class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_islands=0
        def dfs(i,j):
            # Base case
            if i<0 or i>=h or j<0 or j>=w:
                return
            if grid[i][j]=="0":
                return
            grid[i][j]="0"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        h,w=len(grid),len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j]=="1":
                    dfs(i,j)
                    num_islands+=1
        return num_islands


if __name__ == '__main__':
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    sol=Solution()
    res=sol.numIslands(grid)
    print(res)