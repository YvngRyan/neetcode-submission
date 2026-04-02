class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        for pos, sp in pair:
            time = (target - pos) / sp

            if not stack or (stack and stack[-1] < time):
                stack.append(time)
            
        return len(stack)