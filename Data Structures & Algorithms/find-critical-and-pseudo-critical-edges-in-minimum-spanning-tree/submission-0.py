class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1
    
    def find(self, p):
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)
        
        edges.sort(key= lambda e: e[2])

        uf = UnionFind(n)
        mstWeight = 0
        for n1, n2, weight, i in edges:
            if uf.union(n1, n2):
                mstWeight += weight
        
        critical, pseudo = [], []
            
        for n1, n2, weight, i in edges:
            # Try without current edge
            currWeight = 0
            uf = UnionFind(n)
            for n3, n4, weight2, j in edges:
                if i != j and uf.union(n3, n4):
                    currWeight += weight2

            if max(uf.rank.values()) != n or currWeight > mstWeight:
                critical.append(i)
                continue
            
            # Try with current edge
            currWeight = weight
            uf = UnionFind(n)
            uf.union(n1, n2)
            for n3, n4, weight2, j in edges:
                if uf.union(n3, n4):
                    currWeight += weight2
            if currWeight == mstWeight:
                pseudo.append(i)
        return [critical, pseudo]