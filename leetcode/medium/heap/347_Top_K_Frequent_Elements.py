class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for key, val in count.items():
            heapq.heappush(heap, (key, val))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [pair[1] for pair in heap]