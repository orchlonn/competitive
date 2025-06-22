# Brute force solution: 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    res += 1
        return res

# Time complexity: O(N^2)
# Space complexity: O(1)


# Solution #2:
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0 : 1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
        return res

# Time complexity: O(N)
# Space complexity: O(N)