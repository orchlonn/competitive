class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        REd, BLUE = 0, 1
        graph = defaultdict(lambda: defaultdict(list))

        for u, v in redEdges:
            # for directed graph, connect one to one 
            graph[RED][u].append(v)
        for u, v in blueEdges:
            graph[BLUE][u].append(v)
        
        queue = deque([(0, RED, 0), (0, BLUE, 0)])
        visit = {(0, RED), (0, BLUE)}
        ans = [float('inf')] * n

        while queue:
            node, color, steps = queue.popleft()
            ans[node] = min(ans[node], steps)

            for nei in graph[color][node]:
                if (nei, 1 - color) not in visit:
                    queue.append(node, 1- color, steps + 1)
                    visit.add((nei, 1 - color))
            
        return [x if x != float('inf') else -1 for x in ans]