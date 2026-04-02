class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        mp = {}

        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        
        for num, cnt in mp.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res