class Union:
    def __init__(self, n):
        self.par = {}
        self.nodes = {}

        for i in range(n):
            self.par[i] = i
            self.nodes[i] = 1
    
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
        
        if self.nodes[p1] > self.nodes[p2]:
            self.par[p2] = p1
            self.nodes[p1] += self.nodes[p2]
        else:
            self.par[p1] = p2
            self.nodes[p2] += self.nodes[p1]

        return True
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        uf = Union(n)
        for n1, n2 in edges:
            if not uf.union(n1, n2):
                return False

        return True