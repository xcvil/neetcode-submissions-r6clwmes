class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        res = n
        dp = [[False] * n for _ in range(n)] #2D DP map

        for i in range(n):
            dp[i][i] = True
    

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j] and (j-i == 1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1
        return res
