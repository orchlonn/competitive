class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)

        def dfs(node):
            print(node)
            for nei in graph[node]:
                print(graph[node])
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        # build graph
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        ans = 0
        seen = set()
        # cound the province
        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)

        return ans