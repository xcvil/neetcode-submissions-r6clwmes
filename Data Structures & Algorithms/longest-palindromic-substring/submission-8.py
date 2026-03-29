class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        res = ""
        dp = [[False] * n for _ in range(n)]
        dp[n-1][0] = True if s==s[::-1] else False

        for i in range(n):
            dp[i][i] = True
            if len(res) < 1:
                res = s[i]
         
        for i in range(n-2, -1, -1):
            for j in range(1, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > len(res):
                        res = s[i: j+1]
        return res
        