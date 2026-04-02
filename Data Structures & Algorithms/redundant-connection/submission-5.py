class Union:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        curr = n
        while curr != self.par[curr]:
            self.par[curr] = self.par[self.par[curr]]
            curr = self.par[curr]
        return curr
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = Union(len(edges))
        
        for n1, n2 in edges:
            if not uf.union(n1, n2):
                return [n1, n2]