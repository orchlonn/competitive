class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def isValid(row, col):
            return row in range(ROWS) and col in range(COLS)

        ROWS, COLS = len(mat), len(mat[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = deque()
        visit = set()

        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 0:
                    queue.append((row, col, 1))
                    visit.add((row, col))

        while queue:
            row, col, steps = queue.popleft()
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if (isValid(new_row, new_col) and (new_row, new_col) not in visit):
                    visit.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))
                    mat[new_row][new_col] = steps
        
        return mat
