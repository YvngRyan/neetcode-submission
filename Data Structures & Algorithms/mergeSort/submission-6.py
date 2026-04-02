# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs, l, r):
        if (r - l + 1) <= 1:
            return pairs
        
        m = (r + l) // 2

        self.mergeSortHelper(pairs, l, m)
        self.mergeSortHelper(pairs, m + 1, r)

        self.merge(pairs, l, m, r)

        return pairs
    
    def merge(self, arr, l, m, r):
        L = arr[l: m + 1]
        R = arr[m + 1: r + 1]

        lPoint = 0
        rPoint = 0
        i = l

        while lPoint < len(L) and rPoint < len(R):
            if L[lPoint].key <= R[rPoint].key:
                arr[i] = L[lPoint]
                lPoint += 1
            else:
                arr[i] = R[rPoint]
                rPoint += 1
            i += 1
        
        while lPoint < len(L):
            arr[i] = L[lPoint]
            lPoint += 1
            i += 1
        while rPoint < len(R):
            arr[i] = R[rPoint]
            rPoint += 1
            i += 1