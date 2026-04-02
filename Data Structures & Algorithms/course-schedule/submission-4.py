class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursePre = defaultdict(list)

        for course, prereq in prerequisites:
            coursePre[course].append(prereq)

        path = set()

        def dfs(course, path):
            if course in path:
                return False

            path.add(course)

            for prereq in coursePre[course]:
                if not dfs(prereq, path):
                    return False
            path.remove(course)
            coursePre[course] = []

            return True

        
        for course in range(0, numCourses):
            if not dfs(course, path):
                return False
        return True