'''
Problem: Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is 
        formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded
        by water.
        Example 1:
            Input:
                        11110
                        11010
                        11000
                        00000
            Output: 1
        Example 2:
            Input:
                        11000
                        11000
                        00100
                        00011
            Output: 3
'''

class CountIslands(object):
    def numIsland(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # Get the dimensions of the grid
        row, col = len(grid), len(grid[0])

        # Created a visited grid
        visited = [[False for _ in range(col)] for _ in range(row)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] != '1' or visited[i][j]:
                return

            visited[i][j] = True
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        count = 0
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
