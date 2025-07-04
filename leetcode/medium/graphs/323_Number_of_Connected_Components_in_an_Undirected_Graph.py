class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visit = set()
        res = 0

        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            for nei in graph[node]:
                dfs(nei)
            
        for node in range(n):
            if node not in visit:
                res += 1
                dfs(node)

        return res

# Time complexity: O(E + V)
# Space complexity: O(E + V)


# Solution #2: (Union Find)
class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.par = [i for i in range(n)]
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n

        for i, j in edges:
            if uf.union(i, j):
                res -= 1
        
        return res