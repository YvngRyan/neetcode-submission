class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def search(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            
            if r == m or c == n:
                return 0
            
            return search(r + 1, c) + search(r, c + 1)
        return search(0, 0)