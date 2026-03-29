class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # def helper(s, e): # not include e
        def helper(s, e): # include e
            
            close, far = 0, 0
            # for i in range(s, e):
            for i in range(s, e+1):
                curr = max(nums[i]+far, close)
                close, far = curr, close
            return close

        return max(helper(0, n-2), helper(1, n-1))