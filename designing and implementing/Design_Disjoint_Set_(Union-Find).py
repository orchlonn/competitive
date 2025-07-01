class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.num_components = n

    # TC: O(1)
    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    # TC: O(1)
    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    # TC: O(1)
    def union(self, x: int, y: int) -> bool:
        root_y, root_x = self.find(y), self.find(x)
        if root_x != root_y:
            if self.size[root_x] > self.size[root_y]:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            else:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            self.num_components -= 1
            return True
        return False
        
    # TC: O(1)
    def getNumComponents(self) -> int:
        return self.num_components
