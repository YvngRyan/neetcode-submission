class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = [ [] for _ in range(len(nums) + 1)]
        mp = {}
        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        
        for num, val in mp.items():
            cnt[val].append(num)
        
        res = []
        for i in range(len(cnt) - 1, -1, -1):
            for num in cnt[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
        