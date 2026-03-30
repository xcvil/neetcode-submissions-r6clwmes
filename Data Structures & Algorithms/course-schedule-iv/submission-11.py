class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preReq = [[False] * numCourses for _ in range(numCourses)]

        for pre, cur in prerequisites:
            preReq[pre][cur] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    preReq[i][j] = preReq[i][j] or (preReq[i][k] and preReq[k][j])

        res = []
        for pre, cur in queries:
            res.append(preReq[pre][cur])

        return res
        