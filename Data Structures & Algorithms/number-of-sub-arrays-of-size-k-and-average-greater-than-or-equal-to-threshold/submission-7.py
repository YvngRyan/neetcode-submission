class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = 0
        res = 0
        l = 0

        for r in range(len(arr)):
            length = r - l + 1
            if length < k:
                currSum += arr[r]
                continue
            elif length > k:
                currSum -= arr[l]
                l += 1
    
            currSum += arr[r]
            avg = currSum / k
            if avg >= threshold:
                res += 1
        return res