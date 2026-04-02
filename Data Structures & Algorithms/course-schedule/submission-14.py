class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjList = { course : [] for course in range(numCourses) }
        for cls, prereq in prerequisites:
            adjList[cls].append(prereq)
            indegree[prereq] += 1
        
        q = collections.deque()
        for n in range(len(indegree)):
            if indegree[n] == 0:
                q.append(n)
        
        finished = 0
        while q:
            node = q.popleft()
            finished += 1
            for prereq in adjList[node]:
                indegree[prereq] -= 1
                if indegree[prereq] == 0:
                    q.append(prereq)
        return finished == numCourses