from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islandCount += 1
                    self.bfs(i, j, grid)

        return islandCount
    
    def bfs(self, i: int, j: int, grid: List[List[str]]):
        queue = deque()
        queue.append((i,j))
        while len(queue) > 0:
            ii, jj = queue.popleft()
            if grid[ii][jj] == "1":
                grid[ii][jj] = "0"
                if ii - 1 >= 0:
                    #up
                    queue.append((ii - 1, jj))
                if ii + 1 < len(grid):
                    #down
                    queue.append((ii + 1, jj))            
                if jj - 1 >= 0:
                    #left
                    queue.append((ii, jj - 1))
                if jj + 1 < len(grid[ii]):
                    #right
                    queue.append((ii, jj + 1))