class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if (num-1) not in nums:
                k = num + 1
                while k in nums:
                    k += 1
                ans = max(ans, k - num)
        return ans