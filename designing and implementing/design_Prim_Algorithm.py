class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for s, d, w in edges:
            adj[s].append([d, w])
            adj[d].append([s, w])
        
        minHeap = [[0, 0]]
        res = 0
        visit = set()

        while len(visit) < n and minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
                
            visit.add(n1)
            res += w1

            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, [w2, n2])
            
        return res if len(visit) == n else -1


# Time complexity: O(E * log(V)) 
    # TC analysis: O(E * log(E)) = O(E * log(V^2)) = O(E * 2log(V)) = O(E * log(V))

# Space complexity: O(E)

