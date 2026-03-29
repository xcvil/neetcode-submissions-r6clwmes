class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        n = len(s)

        if n == 0:
            return 0

        r = 0
        while r < n:
            if s[r] in s[l:r]:
                l = l + s[l:r].index(s[r]) + 1
            maxLen = max(maxLen, (r-l+1))
            r += 1

        return maxLen

