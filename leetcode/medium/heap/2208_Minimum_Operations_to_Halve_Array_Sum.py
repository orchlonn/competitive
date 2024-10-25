import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        heap = [-num for num in nums]
        heapq.heapify(heap)

        ans = 0
        while target > 0:
            ans += 1
            highest_val = heapq.heappop(heap)
            target += highest_val / 2
            heapq.heappush(heap, highest_val / 2)

        return ans