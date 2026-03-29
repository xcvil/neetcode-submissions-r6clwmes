class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {crs : set() for crs in range(numCourses)}

        for crs, pre in prerequisites:
            graph[crs].add(pre)

        state = [0] * numCourses

        def dfs(i):
            if state[i] == 2:
                return True
            if state[i] == 1:
                return False

            state[i] = 1

            for nei in graph[i]:
                if not dfs(nei):
                    return False

            state[i] = 2
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True