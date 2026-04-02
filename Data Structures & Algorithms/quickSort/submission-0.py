# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def quickSortHelper(l, r):
            if r - l + 1 <= 1:
                return pairs
            
            pivot = pairs[r].key
            left = l

            for i in range(l, r):
                if pairs[i].key < pivot:
                    pairs[left], pairs[i] = pairs[i], pairs[left]
                    left += 1
            
            pairs[r], pairs[left] = pairs[left], pairs[r]

            quickSortHelper(l, left - 1)
            quickSortHelper(left + 1, r)
        
        quickSortHelper(0, len(pairs) - 1)
        return pairs