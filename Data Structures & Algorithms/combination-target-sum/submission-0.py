class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, sum):
            print(f"进入 dfs({i}), subset = {subset}, sum={sum}")
            # print(f"进入 dfs({i}), subset = {subset}, id = {id(subset)}, sum={sum}")
            if sum == target:
                res.append(subset.copy())
                return
            
            if i >= len(nums) or sum > target:
                return

            subset.append(nums[i])
            # dfs(i+1, sum+nums[i])
            dfs(i, sum+nums[i])

            subset.pop()
            dfs(i+1, sum)

        dfs(0,0)
        return res