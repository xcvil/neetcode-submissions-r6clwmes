class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        resMin = nums[0]
        resMax = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                resMax, resMin = max(resMin*nums[i], nums[i]), min(resMax*nums[i], nums[i])
            else:
                resMax, resMin = max(resMax*nums[i], nums[i]), min(resMin*nums[i], nums[i])
            res = max(resMax, res)

        return res