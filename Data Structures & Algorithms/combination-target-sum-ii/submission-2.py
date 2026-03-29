class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, sums):
            if sums == target:
                res.append(subset.copy())
                return

            if i >= len(candidates) or sums > target:
                return

            subset.append(candidates[i])
            dfs(i+1, sums+candidates[i])

            subset.pop()
            # 不选 candidates[i]，并且跳过所有相同的值
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1              # ← 关键：跳过重复
            dfs(i+1, sums)

        dfs(0,0)
        return res