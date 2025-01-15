class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        roads = set()
        seen = {0}
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x, y))

        def dfs(node):
            ans = 0
            for nei in graph[node]:
                if nei not in seen:
                    if (node, nei) in roads:
                        ans += 1
                    seen.add(nei)
                    ans += dfs(nei)
            return ans

        return dfs(0)