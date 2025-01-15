class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        N = len(isConnected)
        visit = set()
        res = 0
        
        for i in range(N):
            for j in range(i + 1, N):
                # checking that there is a connection between i and j
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        def dfs(node):
            # for loop to check all the neighbours of the node
            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
        
        for i in range(N):
            if i not in visit:
                visit.add(i)
                res += 1
                dfs(i)
                
        return res