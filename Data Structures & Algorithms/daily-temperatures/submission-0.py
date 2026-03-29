class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        stack = []
        sId = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1]:
                res[sId[-1]] = (i-sId[-1])

                stack.pop()
                sId.pop()
            stack.append(t)
            sId.append(i)

        return res


            
        