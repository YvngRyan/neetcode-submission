class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currTotal = 0
        res = 0
        l = 0

        for r in range(len(arr)):
            length = r - l + 1
            if length < k:
                currTotal += arr[r]
                continue
            elif length > k:
                currTotal -= arr[l]
                l += 1
            
            currTotal += arr[r]
            avg = currTotal / k

            if avg >= threshold:
                res += 1
        return res