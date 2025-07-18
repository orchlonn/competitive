class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        pq = [[-1, start_node]]
        visit = set()

        while pq:
            prob, curr = heapq.heappop(pq)
            if curr == end_node:
                return prob * -1
            visit.add(curr)
            
            for nei, edgeProb in adj[curr]:
                if nei not in visit:
                    heapq.heappush(pq, (prob * edgeProb, nei))
        
        return 0.0

# Time complexity: O(m log(m))
# Space complexity: O(m + n)