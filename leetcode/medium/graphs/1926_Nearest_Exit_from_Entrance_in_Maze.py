class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def isValid(row, col):
            return row in range(ROWS) and col in range(COLS)

        ROWS, COLS = len(maze), len(maze[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        row, col = entrance
        queue = deque([(row, col, 0)])
        visit = set([(row, col)])

        while queue:
            print(queue)
            row, col, steps = queue.popleft() 

            if steps != 0 and (row + 1 == ROWS or row - 1 == -1 or col + 1 == COLS or col - 1 == -1):
                return steps

            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy

                if isValid(next_row, next_col) and (next_row, next_col) not in visit and maze[next_row][next_col] != '+':
                    queue.append((next_row, next_col, steps + 1))
                    visit.add((next_row, next_col))
        
        return -1