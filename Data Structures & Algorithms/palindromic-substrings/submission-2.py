from functools import cache
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i, j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return dfs(i+1, j-1)
        res = 0
        for length in range(1, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if dfs(i, j):
                    res += 1

        return res
                