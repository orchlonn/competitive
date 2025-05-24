class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def dfs(i):
            if i == len(days):
                return 0
            
            if i in cache:
                return cache[i]
            
            j = i
            res = float("inf")
            for cost, duration in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                res = min(res, cost + dfs(j))
            cache[i] = res
            return cache[i]
            
        cache = {}
        return dfs(0)