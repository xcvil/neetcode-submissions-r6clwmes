class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        need = len(set(t))
        have = 0
        minLen = len(s)+1 # FIX: use n+1 so any valid window is smaller
        res = []

        cT = {}
        cW = {}
        for i in t:
            cT[i] = 1 + cT.get(i, 0)
            cW[i] = 0

        l = 0
        for r in range(len(s)):
            if s[r] in cT:
                cW[s[r]] += 1

                if cW[s[r]] == cT[s[r]]:
                    have += 1
                
                while have == need:
                    if (r-l+1) <= minLen:
                        minLen = (r-l+1)
                        res = [l, r]
                    if s[l] in cT:
                        cW[s[l]] -= 1
                        if cW[s[l]] < cT[s[l]]:
                            have -= 1

                    l += 1

        return s[res[0]: (res[-1]+1)] if res else ""