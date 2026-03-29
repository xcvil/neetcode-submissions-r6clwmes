class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sumN = sum(nums)
        amount = sumN//2

        if sumN % 2 != 0:
            return False

        dp = [False] * (amount+1)

        dp[0] = True

        for num in nums:
            for i in range(amount, num-1, -1):
                dp[i] = dp[i-num] or dp[i]

        return dp[amount]