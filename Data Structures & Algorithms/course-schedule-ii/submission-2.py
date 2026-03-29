class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preHash = {i: [] for i in range(numCourses)}
        taken = []
        visited = set()

        for crs, pre in prerequisites:
            preHash[crs].append(pre)

        # DFS
        def dfs(crs):
            if crs in visited:
                return False
            if crs in taken:
                return True
            if preHash[crs] == []:
                taken.append(crs)
                return True

            visited.add(crs)

            for pre in preHash[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            preHash[crs] = []
            taken.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        
        return taken