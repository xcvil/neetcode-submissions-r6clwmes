class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        left_prod, right_prod = 1, 1
        for i in range(len(nums)):
            ans[i] = left_prod
            left_prod *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= right_prod
            right_prod *= nums[i]

        return ans

        