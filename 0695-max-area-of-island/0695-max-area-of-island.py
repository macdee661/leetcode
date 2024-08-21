from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_size = 0

        def island_size(row, col):
            area = 1
            visited.add((row, col))
            queue = deque([(row, col)])
            directions = [[0,1], [1,0], [0,-1], [-1,0]]
            while len(queue) > 0:
                r, c = queue.popleft()
                visited.add((r,c))
                for dr, dc in directions:
                    drow, dcol = r+dr, c+dc
                    if drow in range(rows) and dcol in range(cols) and grid[drow][dcol] == 1 and (drow, dcol) not in visited:
                        queue.append((drow,dcol))
                        visited.add((drow, dcol))
                        area += 1
            return area


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_size = max(island_size(row, col), max_size)
        return max_size

