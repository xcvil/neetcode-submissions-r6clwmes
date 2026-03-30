class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = collections.defaultdict(set)

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
            res.append(dfs(cur, pre))

        return res