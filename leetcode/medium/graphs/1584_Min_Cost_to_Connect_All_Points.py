class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0 
        minHeap = [[0, 0]]
        visit = set()

        while minHeap and len(visit) < N:
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
                
            visit.add(node)
            res += cost

            for neiCost, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])                
            
        return res

# Time complexity: O(N^2 * log(N))
# Space complexity: O(N^2)