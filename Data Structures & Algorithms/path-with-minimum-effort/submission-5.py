class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        import heapq
        heap = [(0, 0, 0)]
        move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        row, col = len(heights), len(heights[0])

        efforts = [[float('inf')] * col for _ in range(row)]

        efforts[0][0] = 0

        while heap:
            effort, r, c = heapq.heappop(heap)
            if effort > efforts[r][c]: continue
            for dr, dc in move:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < row and nc >=0 and nc < col:
                    new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))


        return efforts[-1][-1]