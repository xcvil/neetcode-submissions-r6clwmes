class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        beingTrusted = {i: 0 for i in range(1, n+1)}
        toTrust = {i: 0 for i in range(1, n+1)}
        for pre, tru in trust:
            beingTrusted[tru] += 1
            toTrust[pre] += 1

        for i in range(1, n+1):
            if toTrust[i] == 0 and beingTrusted[i] == n-1:
                return i

        return -1

        