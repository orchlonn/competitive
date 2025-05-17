class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)

        for i in range(len(nums), -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res[i] = max(res[i], 1 + res[j])
            
        return max(res)


# Time complexity: O(N^2)
# Space complexity: O(N)


# Solution #2: (Bottom up solution optimized by binary search)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for num in nums:
            index = bisect.bisect_left(sub, num)

            if index == len(sub):
                sub.append(num)
            else:
                sub[index] = num

        return len(sub)

# Time complexity: O(N log(N))
# Space complexity: O(N)