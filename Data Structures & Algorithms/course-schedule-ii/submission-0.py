class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = { n : [] for n in range(numCourses) }
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        courses = []

        visit = set()

        def topSort(crs):
            if crs in path:
                return False
            if crs in visit:
                return True
            
            path.add(crs)
            for pre in adjList[crs]:
                if not topSort(pre):
                    return False
            
            path.remove(crs)
            visit.add(crs)
            courses.append(crs)
            return True
        
        path = set()
        for n in range(numCourses):
            if topSort(n) == False:
                return []
        
        return courses