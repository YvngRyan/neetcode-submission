class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in count:
                return [count[diff], i]
            count[num] = i
        return []