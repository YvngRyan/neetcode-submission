class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Go through the array and keep track in an array of length nums
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                    res.append(n)
                    if len(res) == k:
                        return res