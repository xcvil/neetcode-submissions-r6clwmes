class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isPrereq = [[False] * numCourses for _ in range(numCourses)]

        for pre, crs in prerequisites:
            isPrereq[crs][pre] = True

        for k in range(numCourses):
            for crs in range(numCourses):
                for pre in range(numCourses):
                    isPrereq[crs][pre] = isPrereq[crs][pre] or (isPrereq[crs][k] and isPrereq[k][pre])

        res = []

        for pre, crs in queries:
            res.append(isPrereq[crs][pre])

        return res