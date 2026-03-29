class Solution:
    def rob(self, nums: List[int]) -> int:

        # n = len(nums)
        # if n >= 2:
        #     nums[1] = max(nums[0], nums[1])
        #     for i in range(2, n):
        #         nums[i] = max(nums[i-2]+nums[i], nums[i-1])

        # return nums[-1]
        
        rob1, rob2 = 0, 0

        for num in nums:
            tmp = max(num + rob1, rob2)
            rob1, rob2 = rob2, tmp
        return rob2

# from functools import cache
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         @cache
#         def dfs(i):
#             if i >= n:
#                 return 0
#             return max(dfs(i+1), nums[i]+dfs(i+2))
#         return dfs(0)