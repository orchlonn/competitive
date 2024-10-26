import heapq

# Solution 1
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
            
        return heap[0]


# Solution 2
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]

        heapq.heapify(heap)
        ans = 0
        while k > 0:
            ans = heapq.heappop(heap)
            k -= 1

        return -ans