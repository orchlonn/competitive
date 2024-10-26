import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)

        ans = 0
        while sticks:
            first = heapq.heappop(sticks)
            if 1 > len(sticks):
                return ans
            second = heapq.heappop(sticks)
            temp = first + second
            heapq.heappush(sticks, temp)
            ans += temp