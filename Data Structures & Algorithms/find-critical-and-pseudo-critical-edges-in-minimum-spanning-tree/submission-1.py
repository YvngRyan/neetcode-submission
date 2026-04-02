class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.rank = {}

        for i in range(n):
            self.parents[i] = i
            self.rank[i] = 1
    
    def find(self, n):
        curr = n
        while curr != self.parents[curr]:
            self.parents[curr] = self.parents[self.parents[curr]]
            curr = self.parents[curr]
        return curr
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parents[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i) # ex: [node1, node2, weight, index]


        edges.sort(key= lambda e: e[2])

        mstWeight = 0
        uf = UnionFind(n)
        for n1, n2, weight, i in edges:
            if uf.union(n1, n2):
                mstWeight += weight
        
        critical, pseudo = [], []

        for n1, n2, weight, i in edges:
            # Exclude current edge
            currMSTWeight = 0
            uf = UnionFind(n)
            for v1, v2, currWeight, j in edges:
                if i != j and uf.union(v1, v2):
                    currMSTWeight += currWeight
            
            if max(uf.rank.values()) != n or currMSTWeight > mstWeight:
                critical.append(i)
                continue
            
            # This isn't critical, so check if pseudo
            uf = UnionFind(n)
            uf.union(n1, n2)
            currMSTWeight = weight
            for v1, v2, currWeight, j in edges:
                if uf.union(v1, v2):
                    currMSTWeight += currWeight
            
            if currMSTWeight == mstWeight:
                pseudo.append(i)
        return [critical, pseudo]