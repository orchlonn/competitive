class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dest in roads:
            graph[src].append(dest)
            graph[dest].append(src)
        
        res = 0
        for c1, c2 in combinations(graph.keys(), 2):
            connection = 1 if c1 in graph[c2] else 0
            c1_connection = len(graph[c1])
            c2_connection = len(graph[c2])
            res = max(res, c1_connection + c2_connection - connection)

        return res