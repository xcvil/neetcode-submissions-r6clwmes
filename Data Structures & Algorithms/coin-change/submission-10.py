class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from functools import cache
        @cache
        def dfs(remaining):
            if remaining == 0:
                return 0
            res = float('inf')

            for coin in coins:
                if coin <= remaining:
                    res = min(res, 1+dfs(remaining-coin))

            return res

        res = dfs(amount)
        return res if res != float('inf') else -1


