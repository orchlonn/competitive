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
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1 
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums_to_index = {}
        uf = UnionFind(len(nums))

        for i, num in enumerate(nums):
            if num not in nums_to_index:
                nums_to_index[num] = i
        
        for num in nums_to_index:
            if (num + 1) in nums_to_index:
                uf.union(nums_to_index[num], nums_to_index[num + 1])
        
        return max(uf.rank)


# Time complexity: O(N)
# Space complexity: O(N)