class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append([b, values[i]])
            graph[b].append([a, 1 / values[i]])
        
        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1
            
            queue, visit = deque(), set()
            queue.append((src, 1))
            visit.add((src))
            while queue:
                node, val = queue.popleft()
                if node == target:
                    return val
                
                for nei, weight in graph[node]:
                    if nei not in visit:
                        visit.add((nei))
                        queue.append((nei, val * weight))
            
            return -1
        
        return [bfs(q[0], q[1]) for q in queries]