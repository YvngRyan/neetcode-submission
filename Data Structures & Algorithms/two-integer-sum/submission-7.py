class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {};

        for n in range(len(nums)):
            diff = target - nums[n];
            if diff in mp:
                return [mp[diff], n];
            mp[nums[n]] = n