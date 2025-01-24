class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def isValid(row, col):
            return row in range(ROWS) and col in range(COLS)

        ROWS, COLS = len(mat), len(mat[0]) 
        queue = deque()
        visit = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 0:
                    queue.append((row, col, steps))
                    visit.add((row, col))
        
        while queue:
            row, col, steps = queue.popleft()
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if isValid(next_row, next_col) and (next_row, next_col) not in visit:
                    queue.append((next_row, next_col, steps + 1))
                    visit.add((next_row, next_col))
                    mat[next_row][next_col] = steps
        
        return mat