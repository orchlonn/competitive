class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visit = set()
        graph = defaultdict(list)
        ans = 0
      
        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
                    
        def dfs(node):
            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
                    
        for i in range(N):
            if i not in visit:
                ans += 1
                visit.add(i)
                dfs(i)
    
        return ans