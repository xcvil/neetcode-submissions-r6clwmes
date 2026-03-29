class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i: set() for i in range(numCourses)}

        for pre, cur in prerequisites:
            graph[cur].add(pre)

        def dfs(start, end):
            if start == end:
                return True

            if start in visited:
                return False

            visited.add(start)

            for nei in graph[start]:
                # if nei not in visited:
                #     if not dfs(nei, end):
                #         return False
                if dfs(nei, end):
                    return True
            return False

        res = []
        for pre, cur in queries:
            visited = set()
            res.append(dfs(cur, pre))

        return res