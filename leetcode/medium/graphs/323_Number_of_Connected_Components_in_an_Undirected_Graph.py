class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()
        ans = 0
        
        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        
        for node in range(n):
            if node not in visit:
                ans += 1
                dfs(node)
        
        return ans