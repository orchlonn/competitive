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