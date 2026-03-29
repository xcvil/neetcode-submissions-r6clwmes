class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sumN = sum(nums)
        amount = sumN//2

        if sumN % 2 != 0:
            return False
        dp = [[False] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(amount+1):
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

        return dp[n][amount]



        

        