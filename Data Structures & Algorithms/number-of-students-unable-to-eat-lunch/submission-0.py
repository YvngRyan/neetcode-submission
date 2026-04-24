class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        countStudents = { 0 : 0, 1 : 0 }
        
        res = len(students)
        for s in students:
            countStudents[s] += 1
        
        for s in sandwiches:
            if countStudents[s] > 0:
                res -= 1
                countStudents[s] -= 1
            else:
                break
        return res
        
