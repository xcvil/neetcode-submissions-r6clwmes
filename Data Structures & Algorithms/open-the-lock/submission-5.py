class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0

        front = {"0000"}
        back = {target}
        visited = {"0000", target}
        res = 0

        while front and back:
            if len(front) > len(back):
                front, back = back, front

            next_front = set()
            for currComb in front:
                for k in range(4):
                    d = int(currComb[k])

                    for delta in (1, -1):
                        nei = str((d+delta)%10)
                        nextComb = currComb[:k] + nei + currComb[k+1:]

                        if nextComb in back:
                            return res+1

                        if nextComb not in visited and nextComb not in deadends:
                            next_front.add(nextComb)
                            visited.add(nextComb)

            res += 1
            front = next_front

        return -1