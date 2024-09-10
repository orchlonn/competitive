# Solution 1: 
# time complexity: 0(n^2)
# space complexity: 0(n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_arr = []

        i = 0
        for j in matrix:
            for n in j:
                new_arr.append(n)
        
        return self.searchTarget(new_arr, target)

    def searchTarget(self, sorted_arr, target):
        l, r = 0, len(sorted_arr) - 1

        while l <= r:
            mid = (l + r) // 2

            if sorted_arr[mid] > target:
                r = mid - 1
            elif sorted_arr[mid] < target:
                l = mid + 1 
            else:
                return True
        
        return False

# Solution 2:
# time complexity: 0(logN)
# space complexity: 0(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, n * m - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // n
            col = mid % n
            num = matrix[row][col]

            if num == target:
                return True

            if target > num:
                l = mid + 1
            else:
                r = mid - 1
        
        return False