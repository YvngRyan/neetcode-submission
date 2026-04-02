class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = set()

        for n in nums:
            if n in count:
                return n
            count.add(n)