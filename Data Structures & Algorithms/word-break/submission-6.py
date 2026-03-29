from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        startDict = defaultdict(List)
        if s in wordDict:
            return True
        @cache
        def dfs(start):

            if start == len(s):
                return True
            success = False
            for i in range(start, len(s)):
                if s[start:i+1] in wordDict:
                    success = (success or dfs(i+1))
                else:
                    continue
            return success
        return dfs(0)