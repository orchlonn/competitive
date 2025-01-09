class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        visit = set((0, 0))
        queue = deque([(0, 0, 1)])

        while queue:
            r, c, length = queue.popleft()
            if (grid[r][c] == 0 or
                r not in range(N) or
                c not in range(N)
            ):
                continue

            if r == N - 1 and c == N - 1:
                return length

            for dx, dy in directions:
                if (r + dx, c + dy) not in visit and grid[r][c] == 1:
                    visit.add((r + dx, c + dy))
                    queue.append((r + dx, c + dy, length + 1))
            
        return -1