class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        roads = set()
        seen = {0}
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
            roads.add((i, j))
        
        def dfs(node):
            res = 0
            for nei in graph[node]:
                if nei not in seen:
                    if (nei, node) not in roads:
                        res += 1
                    seen.add(nei)
                    res += dfs(nei)
            return res
        
        return dfs(0) 