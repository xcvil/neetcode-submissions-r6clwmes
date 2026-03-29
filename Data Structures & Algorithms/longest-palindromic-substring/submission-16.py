class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        res = s[0]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j] and (j-i<= 2 or dp[i+1][j-1]): # garantee that i+1>=j-1 -> return True
                # if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if (j-i+1) > len(res):
                        res = s[i:j+1]
        return res