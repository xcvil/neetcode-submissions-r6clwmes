class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def robb(start, end):
            a, b = 0, 0
            for i in range(start, end):
                tmp = max(a+nums[i], b)
                a, b = b, tmp
            return b

        return max(robb(0, n-1), robb(1, n))