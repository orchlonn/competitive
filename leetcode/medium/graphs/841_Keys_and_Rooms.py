class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(rooms)):
            graph[i] = rooms[i]
        
        def dfs(node):
            visit.add((node))
            for nei in graph[node]:
                if nei not in visit:
                    dfs(nei)
        
        visit = set()
        dfs(0)
        return True if len(visit) == len(rooms) else False