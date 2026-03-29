class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        n = len(s)
        have = 0
        lenRes = n
        res = []

        countT = {}
        countW = {}

        for i in t:
            countT[i] = 1 + countT.get(i, 0)
            countW[i] = 0
        need = len(countT)
        l = 0
        for r in range(n):
            if s[r] in countT:
                countW[s[r]] += 1

                if countW[s[r]] == countT[s[r]]:
                    have += 1

            

            while have == need:
                if s[l] in countT:
                    countW[s[l]] -= 1
                    if countW[s[l]] < countT[s[l]]:
                        have -= 1

                if (r-l+1) <= lenRes:
                    lenRes = (r-l+1)
                    res = [l, r]
                l += 1
        return s[res[0]:(res[-1]+1)] if res else ""


            
            
            


        