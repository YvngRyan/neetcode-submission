class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            currTemp = temperatures[i]
            days = 1
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > currTemp:
                    res[i] = days
                    break
                days += 1
        return res