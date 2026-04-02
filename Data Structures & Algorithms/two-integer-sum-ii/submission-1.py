class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        b, e = 0, len(numbers) -1

        while b < e:
            total = numbers[b] + numbers[e]
            if total < target:
                b += 1
            elif total > target:
                e -= 1
            else:
                return [b + 1, e + 1]
        return []
        
        