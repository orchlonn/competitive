class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        visit = set()
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        for i in restricted:
            visit.add(i)
        
        def dfs(node):
            if node in visit:
                return 0
            
            visit.add(node)
            count = 1
            for nei in graph[node]:
                if nei in visit:
                    count += dfs(nei)
            
            return count
        
        return dfs(0)