class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        cnt = 0
        for n in operations:
            if n == '+':
                val = rec[-1] + rec[-2]
                rec.append(val)
                cnt += val
            elif n == 'D':
                val = rec[-1] * 2
                rec.append(val)
                cnt += val
            elif n == 'C':
                val = rec.pop()
                cnt -= val
            else:
                rec.append(int(n))
                cnt += int(n)
        return cnt