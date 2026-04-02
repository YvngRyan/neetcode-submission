class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posToSpeed = {}
        for i in range(len(position)):
            posToSpeed[position[i]] = speed[i]
        position.sort()

        stack = []

        for i in range(len(position) - 1, -1, -1):
            pos = position[i]
            sp = posToSpeed[pos]

            stack.append((target - pos) / sp)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)