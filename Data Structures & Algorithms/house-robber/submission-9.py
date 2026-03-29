class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1]*n

        def dfs(i):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i+1), dfs(i+2)+nums[i])
            return memo[i]

        return dfs(0)