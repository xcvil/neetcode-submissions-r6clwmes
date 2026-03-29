class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preHash = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preHash[crs].append(pre)
        state = [0] * numCourses
        order = []

        def dfs(crs):
            if state[crs] == 1:
                return False
            if state[crs] == 2:
                return True

            state[crs] = 1
            for pre in preHash[crs]:
                if not dfs(pre):
                    return False
            state[crs] = 2
            order.append(crs)
            return True

        for crs in preHash:
            if not dfs(crs):
                return []

        return order