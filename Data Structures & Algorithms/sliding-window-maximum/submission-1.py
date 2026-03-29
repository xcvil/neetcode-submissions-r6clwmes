class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque()
        res = []
        for r in range(len(nums)):
            if dq and (r-dq[0]+1) > k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            if r >= (k-1):
                res.append(nums[dq[0]])

        return res
        