# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        for i in range(len(pairs)):
            r = i
            while r > 0 and pairs[r].key < pairs[r - 1].key:
                    pairs[r], pairs[r - 1] = pairs[r - 1], pairs[r]
                    r -= 1
            res.append(pairs.copy())
        return res