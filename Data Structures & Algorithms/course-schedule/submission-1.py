class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preHash = {crs: [] for crs in range(numCourses)}

        for crs, pre in prerequisites:
            preHash[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if preHash[crs] == []:
                return True

            visited.add(crs)

            for pre in preHash[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            preHash[crs] = []
            
            return True

        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
            