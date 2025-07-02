class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]
        rank = [0] * (N + 1)

        # Time complexity: O(1)
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        # Time complexity: O(1)
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if p1 > p2:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        # Time complexity: O(N)
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


# Time complexity: O(N)
# Space complexity: O(N)