class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for x1, y1 in self.pts:
            if (abs(y1 - y) == abs(x1 - x)) and (x1 != x and y1 != y):
                res += self.points[(x1, y)] * self.points[(x, y1)]
        return res