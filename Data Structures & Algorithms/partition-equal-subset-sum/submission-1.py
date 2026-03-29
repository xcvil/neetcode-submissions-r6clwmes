class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        sumN = sum(nums)

        if sumN % 2 != 0:
            return False
        
        def dfs(i, target):
            if target < 0:
                return False
            
            remaining = target - nums[i]

            if remaining == 0:
                return True
            for j in range(i+1, n):
                if dfs(j, remaining):
                    return True
            return False

        return dfs(0, sumN/2)

            