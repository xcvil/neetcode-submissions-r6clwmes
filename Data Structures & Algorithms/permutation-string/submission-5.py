class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1 = len(s1)
        countS1 = {}
        count = {}
        # O(k)
        for c in s1:
            countS1[c] = 1 + countS1.get(c, 0)

        l = 0
        # O(n)
        for r in range(len(s2)):
            if s2[r] in s1:
                count[s2[r]] = 1 + count.get(s2[r], 0)

                # Shrink window if too large
                while (r - l + 1) > lenS1:
                    count[s2[l]] -= 1
                    if count[s2[l]] == 0:
                        del count[s2[l]]
                    l += 1
                
                # Check if valid permutation
                if count == countS1:
                    return True
            else:
                l = r + 1
                count = {}
            

        return False

        