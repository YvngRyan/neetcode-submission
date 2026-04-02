# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def mergeSortHelper(l, r):
            if r - l + 1 <= 1:
                return pairs
            
            m = (l + r) // 2
            mergeSortHelper(l, m)
            mergeSortHelper(m + 1, r)

            merge(l, m, r)
        def merge(l, m, r):
            arr1 = pairs[l : m + 1]
            arr2 = pairs[m + 1 : r + 1]
            p1 = 0
            p2 = 0

            i = l

            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1].key <= arr2[p2].key:
                    pairs[i] = arr1[p1]
                    p1 += 1
                else:
                    pairs[i] = (arr2[p2])
                    p2 += 1
                i += 1
            
            while p1 < len(arr1):
                pairs[i] = arr1[p1]
                p1 += 1
                i += 1
            while p2 < len(arr2):
                pairs[i] = arr2[p2]
                p2 += 1
                i += 1
            
        mergeSortHelper(0, len(pairs) - 1)
        return pairs