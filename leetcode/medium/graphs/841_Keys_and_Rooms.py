class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        
        for i in range(len(rooms)):
            for j in rooms[i]:
                graph[i].append(j)  
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        return True if len(rooms) == len(visited) else False    