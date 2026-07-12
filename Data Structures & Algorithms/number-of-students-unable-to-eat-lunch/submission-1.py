class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students0 = 0
        students1 = 0

        for s in students:
            if s == 0:
                students0 += 1
            else:
                students1 += 1
        
        for s in sandwiches:
            if s == 0:
                if students0 > 0:
                    students0 -= 1
                else:
                    return students0 + students1
            else:
                if students1 > 0:
                    students1 -= 1
                else:
                    return students0 + students1
        
        return students0 + students1