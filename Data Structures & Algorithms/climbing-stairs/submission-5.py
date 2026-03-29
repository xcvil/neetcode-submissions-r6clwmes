from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def dfs(i):
            if i == n:
                return True
            if i > n:
                return False
            res = 0
            res += dfs(i+1)
            res += dfs(i+2)
            return res

        return dfs(0)

        