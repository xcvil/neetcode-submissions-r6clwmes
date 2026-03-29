class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1Count, winCount = [0]*26, [0]*26
        
        for s in s1:
            idx = int(ord(s)-ord('a'))
            s1Count[idx] += 1

        for s in s2[:len(s1)]:
            idx = int(ord(s)-ord('a'))
            winCount[idx] += 1

        match = 0

        for i in range(26):
            match += (1 if s1Count[i] == winCount[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):

            if match == 26: return True
            idx = int(ord(s2[r]) - ord('a'))
            winCount[idx] += 1
            if winCount[idx] == s1Count[idx]:
                match += 1
            elif winCount[idx] - 1 == s1Count[idx]:
                match -= 1


            idx = int(ord(s2[l]) - ord('a'))
            winCount[idx] -= 1
            if winCount[idx] == s1Count[idx]:
                match += 1
            elif winCount[idx] + 1 == s1Count[idx]:
                match -= 1
            l+=1
        return match == 26
        