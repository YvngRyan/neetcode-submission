class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr = max(-1, arr[-1])
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            tmp = arr[i]
            arr[i] = curr
            curr = max(curr, tmp)
        return arr