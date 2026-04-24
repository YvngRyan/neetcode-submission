class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for crs, prereq in prerequisites:
            adjList[crs].append(prereq)

        visited = set()
        def dfs(n):
            if adjList[n] == []:
                return True
            
            if n in visited:
                return False

            visited.add(n)
            
            for prereq in adjList[n]:
                if not dfs(prereq):
                    return False
            visited.remove(n)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True