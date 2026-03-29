class Solution:
    def permute(self, nums):
        res = []
        subset = []
        used = set()

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for num in nums:
                if num in used:
                    continue
                used.add(num)
                subset.append(num)
                dfs()
                subset.pop()
                used.remove(num)

        dfs()
        return res