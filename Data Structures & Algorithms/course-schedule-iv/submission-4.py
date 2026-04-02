class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = { n : [] for n in range(numCourses) }
        cache = [[-1] * numCourses for _ in range(numCourses)]
        for pre, crs in prerequisites:
            adjList[crs].append(pre)
            cache[crs][pre] = 1

        def dfs(crs, potPre):
            if cache[crs][potPre] != -1:
                return cache[crs][potPre] == 1
            
            for pre in adjList[crs]:
                if pre == potPre or dfs(pre, potPre):
                    cache[crs][potPre] = 1
                    return True
            
            cache[crs][potPre] = 0
            return False

        res = []

        for potPre, crs in queries:
            if dfs(crs, potPre):
                res.append(True)
            else:
                res.append(False)
        
        return res