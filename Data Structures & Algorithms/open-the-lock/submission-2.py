class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        graph = collections.defaultdict(set)

        for i in range(9):
            graph[str(i)].add(str(i+1))
        
        for i in range(1, 10):
            graph[str(i)].add(str(i-1))
        graph["9"].add("0")
        graph["0"].add("9")

        print(graph)

        visited = set()
        q = collections.deque()
        q.append("0000")
        visited.add("0000")
        res = 0

        while q:
            for _ in range(len(q)):
                currComb = q.popleft()
                if currComb == target:
                    return res

                for k in range(4):
                    currKey = currComb[k]
                    targetKey = target[k]
                    
                    for nei in graph[currKey]:
                        # if nei == targetKey
                        nextComb = currComb[:k]+nei+currComb[k+1:]
                        if nextComb not in visited and nextComb not in deadends:
                            q.append(nextComb)
                            visited.add(nextComb)
            res += 1
        
        return -1
