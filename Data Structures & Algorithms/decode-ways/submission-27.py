class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)
        a, b = 1, 0
        for i in range(n-1, -1, -1):
            if s[i] == "0":
                tmp = 0
            else:
                tmp = a
                if i+1 < n and int(s[i:i+2]) <= 26:
                    tmp += b
            a, b = tmp, a
        return a

