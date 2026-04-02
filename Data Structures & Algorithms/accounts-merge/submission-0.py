class Union:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(len(n)):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        curr = self.par
        p = self.par[n]

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
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = Union(accounts)
        accToIndex = {}
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in accToIndex:
                    uf.union(i, accToIndex[email])
                else:
                    accToIndex[email] = i

        emailGroup = defaultdict(list)
        for email, index in accToIndex.items():
            leader = uf.find(index)
            emailGroup[leader].append(email)
        
        res = []
        for index, emails in emailGroup.items():
            name = accounts[index][0]
            res.append([name] + sorted(emails))
        return res











