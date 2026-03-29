class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i):
            if i >= n:
                return 1, 1
            # res = nums[i]
            # for j in range(i+1, n):
            #     res = max(res, nums[i] * dfs(j))
            if nums[i] >= 0:
                return max(nums[i], nums[i]*dfs(i+1)[0]), min(nums[i], nums[i]*dfs(i+1)[1])
            else:
                return max(nums[i], nums[i]*dfs(i+1)[1]), min(nums[i], nums[i]*dfs(i+1)[0])

        res = float('-inf')
        for i in range(n):
            res = max(res, dfs(i)[0])


        return res