class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i: set() for i in range(numCourses)}
        isPrereq = [[-1] * numCourses for _ in range(numCourses)]

        for pre, crs in prerequisites:
            graph[crs].add(pre)
            isPrereq[crs][pre] = 1

        def dfs(start, end):
            if isPrereq[start][end] != -1:
                return isPrereq[start][end] == 1

            for nei in graph[start]:
                if nei == end or dfs(nei, end):
                    isPrereq[nei][end] = 1
                    return True
            
            isPrereq[start][end] = 0
            return False

        res = []
        for u, v in queries:
            res.append(dfs(v, u))
        return res
