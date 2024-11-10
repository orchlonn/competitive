class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deqeue([(0, 0, 1)]) 
        visit = set((0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], 
                      [1, 1], [-1, -1], [-1, 1], [1, -1]]
        
        while q:
            r, c, length = q.popleft()

            if (min(r, c) < 0 or max(r, c) >= N or grid[r][c] == 1):
                continue
                
            if r == N - 1 and c == N - 1:
                return length

            for dr, dc in directions:
                if (r + dr, c + dc) not in visit:
                    visit.add((r + dr, c + dc))
                    q.append((r + dr, c + dc, length + 1))

        return -1