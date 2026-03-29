from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(i, sum):
            if sum == amount:
                return 0
            if sum > amount or i >= len(coins):
                return float('inf')
            res = float('inf')

            res = min(res, 1 + dfs(i, sum+coins[i]))
            res = min(res, dfs(i+1, sum))
            return res

        res = dfs(0, 0)
        return res if res != float('inf') else -1
