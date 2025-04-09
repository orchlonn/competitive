class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visit = set()
        res = 0

        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            for nei in graph[node]:
                dfs(nei)
            
        for node in range(n):
            if node not in visit:
                res += 1
                dfs(node)

        return res

# Time complexity: O(E + V)
# Space complexity: O(E + V)