from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            visited.add((row, col))
            queue = deque([(row, col)])
            directions = [[1,0], [0,1], [-1,0], [0,-1]]

            while len(queue) > 0:
                r, c = queue.popleft()
                for dr, dc in directions:
                    drow = r+ dr
                    dcol = c + dc
                    if drow in range(rows) and dcol in range(cols) and (drow, dcol) not in visited and grid[drow][dcol] == "1":
                        queue.append((drow, dcol))
                        visited.add((drow, dcol))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    islands += 1

        return islands
