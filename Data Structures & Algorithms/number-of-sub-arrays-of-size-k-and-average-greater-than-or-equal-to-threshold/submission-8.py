class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0

        l, r = 0, 0

        res = 0
        while r < len(arr):
            total += arr[r]

            if r - l + 1 > k:
                total -= arr[l]
                l += 1
            
            if r - l + 1 == k:
                if total / k >= threshold:
                    res += 1
            r += 1
        return res
            
