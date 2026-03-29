class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        n = len(s)
        need = len(set(t))  # BUG 1 FIX: count unique chars, not len(t)
        have = 0
        lenRes = n + 1       # FIX: use n+1 so any valid window is smaller
        res = []

        countT = {}
        countW = {}

        for i in t:
            countT[i] = 1 + countT.get(i, 0)
            countW[i] = 0

        l = 0
        for r in range(n):
            if s[r] in countT:
                countW[s[r]] += 1

                if countW[s[r]] == countT[s[r]]:
                    have += 1

            while have == need:
                if (r - l + 1) <= lenRes:  # FIX: check length before shrinking
                    lenRes = (r - l + 1)
                    res = [l, r]

                if s[l] in countT:
                    countW[s[l]] -= 1
                    if countW[s[l]] < countT[s[l]]:
                        have -= 1

                l += 1  # BUG 2 FIX: move left pointer RIGHT, not left

        return s[res[0]:(res[-1] + 1)] if res else ""  # FIX: handle empty case