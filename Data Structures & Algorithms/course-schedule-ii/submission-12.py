class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {crs : set() for crs in range(numCourses)}

        for crs, pre in prerequisites:
            graph[pre].add(crs)

        state = [0] * numCourses
        order = []

        def dfs(i):
            if state[i] == 2:
                return True
            if state[i] == 1:
                return False

            state[i] = 1
            
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            
            order.append(i)
            state[i] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order[::-1]
