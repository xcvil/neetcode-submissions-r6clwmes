class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from collections import deque
        n = len(isConnected)
        q = deque()
        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                visited.add(i)
                q.append(i)
                count += 1
            while q:
                cur = q.popleft()
                for j in range(n):
                    if isConnected[cur][j] == 1 and j not in visited:
                        q.append(j)
                        visited.add(j)

        return count