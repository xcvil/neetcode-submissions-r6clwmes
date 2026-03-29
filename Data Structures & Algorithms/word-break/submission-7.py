from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        @cache
        def dfs(start):

            if start == len(s):
                return True
            # success = False
            for i in range(start, len(s)):
                if s[start:i+1] in wordDict:
                    # success = (success or dfs(i+1))
                    if dfs(i+1):
                        return True
                else:
                    continue
            return False
        return dfs(0)