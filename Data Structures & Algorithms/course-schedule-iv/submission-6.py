class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = { n : [] for n in range(numCourses) }
        prereqs = {}
        for pre, crs in prerequisites:
            adjList[crs].append(pre)

        def dfs(crs):
            if crs not in prereqs:
                prereqs[crs] = set()

                for pre in adjList[crs]:
                    prereqs[crs] |= (dfs(pre))
                prereqs[crs].add(crs)
            return  prereqs[crs]
        
        for n in range(numCourses):
            dfs(n)

        res = []

        for potPre, crs in queries:
            res.append(potPre in prereqs[crs])
        
        return res