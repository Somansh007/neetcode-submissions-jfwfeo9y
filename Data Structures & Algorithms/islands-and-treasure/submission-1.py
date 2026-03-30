from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        INF = 2147483647

        # Step 1: Add all gates (0s) to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 2: BFS
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < ROWS and 0 <= nc < COLS and
                    grid[nr][nc] == INF):
                    
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))