class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * (n)
    
    def find(self, n):
        if n != self.par[n]:
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {} 

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(emailToAcc[e], i)
                else:
                    emailToAcc[e] = i
        
        emailGroup = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, e in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(e))
        
        return res