class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        dp = [1] * n
        prev = [-1] * n
        max_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

                if dp[i] > dp[max_idx]:
                    max_idx = i
                
        result = []
        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = prev[max_idx]
        
        return result

# Time complexity: O(N^2)
# Space complexity: O(N)