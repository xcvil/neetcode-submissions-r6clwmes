class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        n = len(s)
        charPos = {}

        if n == 0:
            return 0

        for r in range(n):
            if s[r] in charPos and charPos[s[r]] >= l:
                l = charPos[s[r]]+1
            charPos[s[r]] = r
            maxLen = max(maxLen, r-l+1)
        return maxLen

