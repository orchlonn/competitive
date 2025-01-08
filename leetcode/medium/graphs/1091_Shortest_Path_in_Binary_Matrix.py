class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = deque([(0, 0, 1)]) # row, column, length
        visist = set((0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                      [1, -1], [-1, 1], [-1, -1], [1, 1]]

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
                if (r + dx, c + dy) not in visit:
                    queue.append((r + dx, c + dy, length + 1))
                    visit.add((r + dx, c + dy))
            
        return -1 