class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
      graph = defaultdict(list)
      
      for i, j in roads:
        graph[i].append(j)
        graph[j].append(i)
      
      res = 0
      for c1, c2 in combinations(graph.keys(), 2):
        connection = 1 if c1 in graph[c2] else 0
        c1_len = len(graph[c1])
        c2_len = len(graph[c2])
        res = max(res, c1_len + c2_len - connection)
      
      return res
        