class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(current):
            if cache.get(current):
                return cache[current]
            elif current >= n:
                return current == n
            cache[current] = dfs(1+current) + dfs(2+current)
            return cache[current]
        return dfs(0)
        

