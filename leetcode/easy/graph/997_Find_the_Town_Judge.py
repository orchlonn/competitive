class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
      graph = defaultdict(int)
      for src, dest in trust:
        graph[src] -= 1
        graph[dest] += 1
        
      for i in range(1, n + 1):
        if graph[i] == n - 1:
          return i
        
      return -1