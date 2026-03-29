class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        sumN = sum(nums)

        if sumN % 2 != 0:
            return False

        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False

            return dfs(i+1, target-nums[i]) or dfs(i+1, target)
        
        return dfs(0, sumN/2)