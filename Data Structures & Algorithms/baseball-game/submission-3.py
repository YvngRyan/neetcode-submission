class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        cnt = 0
        for n in operations:
            if n == '+':
                cnt += rec[-1] + rec[-2]
                rec.append(rec[-1] + rec[-2])
            elif n == 'D':
                cnt += rec[-1] * 2
                rec.append(rec[-1] * 2)
            elif n == 'C':
                cnt -= rec.pop()
            else:
                rec.append(int(n))
                cnt += int(n)
        return cnt