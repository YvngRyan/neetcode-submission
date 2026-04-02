class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def search(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            
            if r == m or c == n:
                return 0
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            cache[(r, c)] = search(r + 1, c) + search(r, c + 1)
            return cache[(r, c)]
        return search(0, 0)