# BFS solution
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        seen = [False] * n
        seen[source] = True
        queue = deque([source])
        
        while queue:
            curr_node = queue.popleft()
            if curr_node == destination:
                return True
            
            for next_nei in graph[curr_node]:
                if (not seen[next_nei]):
                    seen[next_nei] = True
                    queue.append((next_nei))
        
        return False

# DFS solution
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        seen = [False] * n
        
        def dfs(curr_node):
            if curr_node == destination:
                return True

            if not seen[curr_node]:
                seen[curr_node] = True
                for next_nei in graph[curr_node]:
                    if dfs(next_nei):
                        return True
            return False
        
        return dfs(source)