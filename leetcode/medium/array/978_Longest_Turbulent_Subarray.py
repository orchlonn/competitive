class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        count = sign = res = 0

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                count = count + 1 if sign == 0 else 1
                sign = 1
            elif arr[i] < arr[i + 1]:
                count = count + 1 if sign == 1 else 1
                sign = 0
            else:
                count = 0
                sign = 0
            
            res = max(res, count)
        
        return res + 1

# Time complexity: O(n)
# Space complexity: O(1)