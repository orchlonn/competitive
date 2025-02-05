class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
      
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                
                dist = sqrt((x1 - x2)**2 + (y1 -y2)**2)
                
                if dist <= r1:
                    graph[i].append(j)
                if dist <= r2:
                    graph[j].append(i)
                    
        def dfs(i, visit):
            if i in visit:
                return 0
            visit.add(i)
            for nei in graph[i]:
                dfs(nei, visit)
            return len(visit)
        
        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))
        
        return res
