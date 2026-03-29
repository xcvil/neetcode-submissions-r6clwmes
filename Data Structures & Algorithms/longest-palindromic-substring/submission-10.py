class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        def dfs(i, j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return dfs(i + 1, j - 1)
        res = ""
        for leng in range(1, n+1):
            for i in range(n-leng+1):
                j = i + leng - 1

                if dfs(i, j) and leng > len(res):
                    res = s[i:j+1]
        return res

            

        