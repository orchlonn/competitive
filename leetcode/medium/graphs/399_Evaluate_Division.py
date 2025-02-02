class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
      graph = defaultdict(list)
      for i, eq in enumerate(equations):
        