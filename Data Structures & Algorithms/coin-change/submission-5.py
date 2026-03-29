from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')

            res = float('inf')
            for coin in coins:
                res = min(res, 1+dfs(remaining-coin))
            return res

        res = dfs(amount)
        return res if res != float('inf') else -1