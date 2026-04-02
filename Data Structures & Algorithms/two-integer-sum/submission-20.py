class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numCount = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numCount:
                return [numCount[diff], i]
            numCount[nums[i]] = i
        return []