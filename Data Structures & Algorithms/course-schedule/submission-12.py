class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = { n : [] for n in range(numCourses) }

        for crs, prereq in prerequisites:
            adjList[crs].append(prereq)

        def backtrack(n):
            if n in path:
                return False
            
            if adjList[n] == []:
                return True
            
            path.add(n)
            for pre in adjList[n]:
                if not backtrack(pre):
                    return False
            adjList[n] = []
            path.remove(n)
            return True

        path = set()
        for n in range(numCourses):
            if not backtrack(n):
                return False
        return True