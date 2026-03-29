class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        from functools import cache
        @cache
        def dfs(i):
            if i >= n:
                return 0
            # if i == n-1:
            #     return cost[-1]

            res = cost[i]
            return min(res+dfs(i+1), res+dfs(i+2))

        return min(dfs(0), dfs(1))