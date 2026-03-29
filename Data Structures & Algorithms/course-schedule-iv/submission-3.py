class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i: set() for i in range(numCourses)}

        for pre, cur in prerequisites:
            graph[cur].add(pre)

        def dfs(start, end):
            if start == end:
                return True
            visited.add(start)

            for nei in graph[start]:
                if nei not in visited:
                    if dfs(nei, end):
                        return True
            return False

        res = []
        for pre, cur in queries:
            visited = set()
            canReach = dfs(cur, pre)
            if canReach:
                graph[cur].add(pre)
            res.append(canReach)

        return res