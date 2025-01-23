class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = deque([(0, 0, 1)])
        visit = set((0, 0))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], 
                      [1, 1], [-1, -1], [1, -1], [-1, 1]]

        while queue:
            r, c, length = queue.popleft()

            if (r not in range(N) or
                c not in range(N) or
                grid[r][c] == 1 
            ):
                continue

            if r == N - 1 and c == N - 1:
                return length
            
            for dx, dy in directions:
                row, col = r + dx, c + dy
                if (row, col) not in visit and grid[r][c] == 0:
                    visit.add((row, col))
                    queue.append((row, col, length + 1))
            
        return -1
