class Solution:
    def longestPalindrome(self, s: str) -> str:
        def dfs(i, j):
            if i > j:
                return True

            if s[i] != s[j]:
                return False

            return dfs(i+1, j-1)

        n = len(s)
        for length in range(n, 0, -1):       # 先试最长的
            for i in range(n - length + 1):   # 所有起点
                j = i + length - 1
                if dfs(i, j):
                    return s[i:j+1]
        return ""
