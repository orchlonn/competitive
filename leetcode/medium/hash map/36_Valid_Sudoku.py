class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap, colMap = defaultdict(list), defaultdict(list)
        boxMap = defaultdict(list)
        visited = set()

        def dfs(row, col, maxRow, maxCol):
            if row >= maxRow or col >= maxCol:
                return True
            if (row, col) in visited:
                return True
            
            visited.add((row, col))    
            val = board[row][col]

            if val == ".":
                return dfs(row + 1, col, maxRow, maxCol) and dfs(row, col + 1, maxRow, maxCol)

            boxKey = (row // 3, col // 3)
            if (val in boxMap.get(boxKey, set())) or (val in colMap.get(col, set())) or (val in rowMap.get(row, set())):
                return False
            
            boxMap.setdefault(boxKey, set()).add(val)
            colMap.setdefault(col, set()).add(val)
            rowMap.setdefault(row, set()).add(val)

            print(rowMap)
            return dfs(row, col + 1, maxRow, maxCol) and dfs(row + 1, col, maxRow, maxCol)

        for row in range(len(board) - 2):
            for col in range(len(board[0]) - 2):
                if not dfs(row, col, row + 3, col + 3):
                    return False
            
        return True

# Time complexity: O(n^3)
# Space complexity: O(n^2)


# Optimized solution:
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                
                if (val in rows[row] or val in cols[col] or val in squares[row // 3, col // 3]):
                    return False
                
                cols[col].add(val)
                rows[row].add(val)
                squares[row // 3, col // 3].add(val)
                
                print(squares)
                print(rows)
        
        return True

# Time complexity: O(n^2)
# Space complexity: O(n^2)