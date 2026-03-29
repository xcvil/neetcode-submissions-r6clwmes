class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)


        def dfs(i):
            if i >= n:
                return 1
            if s[i] == "0":
                return 0
            if i+1<n and int(s[i:i+2])<=26:
                res = dfs(i+1) + dfs(i+2)
            else:
                res = dfs(i+1)

            return res
        return dfs(0)
