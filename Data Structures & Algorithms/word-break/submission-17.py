from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        @cache
        def dfs(i):
            if i >= n:
                return True

            for j in range(i+1, n+1):
                if s[i:j] in wordDict:
                    if dfs(j):
                        return True
            return False

        return dfs(0)