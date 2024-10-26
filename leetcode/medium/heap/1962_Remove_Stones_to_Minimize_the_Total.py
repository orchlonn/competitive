import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)

        while k > 0 and heap:
            temp = heapq.heappop(heap)
            temp = math.floor(temp / 2)
            heapq.heappush(heap, temp)
            k -= 1
        
        return -sum(heap)