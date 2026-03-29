class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        lenDict = [len(word) for word in wordDict]

        dp = [False] * (n+1)
        dp[n] = True

        for i in range(n-1, -1, -1):
            for leng, word in zip(lenDict, wordDict):
                if leng + i <= n and s[i: leng+i] == word and dp[leng+i]:
                    dp[i] = True

        return dp[0]

