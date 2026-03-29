from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # @cache
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= j:
                return True
            if s[i] != s[j]:
                memo[(i, j)] = False
                return False
            memo[(i, j)] = dfs(i + 1, j - 1)
            return memo[(i, j)]

        n = len(s)
        for length in range(n, 0, -1):       # 先试最长的
            for i in range(n - length + 1):   # 所有起点
                j = i + length - 1
                if dfs(i, j):
                    return s[i:j+1]
        return ""
