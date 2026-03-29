class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob(start, end):
            a, b = 0, 0
            for i in range(start, end):
                tmp = max(a+nums[i], b)
                a, b = b, tmp
            return b

        return max(rob(0, n-1), rob(1, n))