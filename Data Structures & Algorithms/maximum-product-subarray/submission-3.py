class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[1] * len(nums) for _ in range(len(nums))]

        # [len1:[]]

        dp[0] = nums

        # dp[len][start]
        res = max(nums)

        
        for length in range(1, len(nums)):
            for start in range(len(nums)):
                if (start + length) < len(nums):
                    dp[length][start] = dp[length-1][start]*dp[0][start+length]
                    res = max(res, dp[length][start])


        return res

            