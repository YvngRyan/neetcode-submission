class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)

        for course, prereq in prerequisites:
                courses[course].append(prereq)
        path = set()
        def dfs(course):
            if course in path:
                return False

            if courses[course] == []:
                return True
            
            path.add(course)
            for prereq in courses[course]:
                if not dfs(prereq):
                    return False
            courses[course] = []
            path.remove(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
