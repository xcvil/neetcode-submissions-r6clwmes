from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(curr):
            # if curr == n-1:
            #     return 1
            res = 0
            for i in range(curr+1, n):
                if nums[i] > nums[curr]:
                    res = max(res, dfs(i))
            return res+1

        res = 0
        for i in range(n):
            res = max(res, dfs(i))
        return res


                


