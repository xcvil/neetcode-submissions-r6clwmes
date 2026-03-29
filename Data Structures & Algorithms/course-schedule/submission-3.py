class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : set() for i in range(numCourses)}

        for c, prev in prerequisites:
            graph[prev].add(c)
        visited = set()

        def dfs(i):
            if i in visited:
                return False
            if graph[i] == []:
                return True
            visited.add(i)
            for nei in graph[i]:
                if not dfs(nei):
                    return False

            visited.remove(i)
            graph[i] =[]
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        