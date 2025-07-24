class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dest in edges:
            adj[src].append(dest)
        
        visited = set()
        visiting = set()
        topSort = []

        def dfs(src):
            if src in visited:
                return True
            if src in visiting:
                return False
            
            visiting.add(src)
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            
            visiting.remove(src)
            visited.add(src)
            topSort.append(src)

            return True

        for i in range(n):
            if not dfs(i):
                return []
        topSort.reverse()
        return topSort