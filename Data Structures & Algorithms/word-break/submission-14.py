class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lenDict = [len(word) for word in wordDict]
        dp = [False] * (len(s)+1)
        dp[-1] = True
        
        start = len(s) - 1
        for start in range(len(s)-1, -1, -1):
            for word, length in zip(wordDict, lenDict):
                if s[start:start+length] == word and start + length <= len(s) and dp[start+length]: 
                    dp[start] = True
                
        return dp[0]
                    
                