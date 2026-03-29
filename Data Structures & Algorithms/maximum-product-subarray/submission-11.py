class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        preMax = nums[0]
        preMin = nums[0]
        res = nums[0]

        for i in range(1, n):
            if nums[i] < 0:
                preMax, preMin = max(preMin*nums[i], nums[i]), min(preMax*nums[i], nums[i])
            else:
                preMax, preMin = max(preMax*nums[i], nums[i]), min(preMin*nums[i], nums[i])

            res = max(res, preMax)
        return res